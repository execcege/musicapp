var tag = document.createElement('script');

tag.src = "https://apis.google.com/js/client.js?onload=onClientLoad";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);


var apiLoaded = false;

// Called automatically when JavaScript client library is loaded.
function onClientLoad() {
    gapi.client.load('youtube', 'v3', onYouTubeApiLoad);
    //search();    // changed.
}

// Called automatically when YouTube API interface is loaded (see line 9).
function onYouTubeApiLoad() {
    // This API key is intended for use only in this lesson.
    // See http://goo.gl/PdPA1 to get a key for your own applications.
    gapi.client.setApiKey('AIzaSyD49-XZ2JV7Rws3KDM2T7nA56Jbi-O7djY');
    console.log("YOUTUBE API LOADED");
    apiLoaded = true;
}


angular.module('musicApp', ['ngRoute', 'ui.bootstrap'])
    .config(function($routeProvider) {
        $routeProvider
            .when('/', {
                controller:'musicController',
                templateUrl:'resources/client/client.html'
            })
            .otherwise({
                redirectTo:'/'
            });
    })
    .controller('musicController', ['$scope', '$modal', '$timeout', '$http', function($scope, $modal, $timeout, $http) {
        $scope.query = "";
        $scope.apiLoading = !apiLoaded;
        $scope.loading = false;
        $scope.searchResult = [];
        $scope.added = [];

        $scope.searchQuery = "";
        $scope.searchYT = function(){
            if($scope.query != "") {
                $scope.loading = true;
                var request = gapi.client.youtube.search.list({
                    q: $scope.query,
                    part: 'snippet',
                    maxResults: 50
                });

                request.execute(function (response) {
                    $scope.searchResult = response.result.items;
                    $scope.loading = false;
                    $scope.$apply();
                });
            }
        };

        $scope.checkApiStatus = function(){
          if (apiLoaded){
              console.log("loaded");
              $scope.apiLoading = false;
              $scope.$apply()
          }
          else{
              console.log("not loaded");
              $timeout($scope.checkApiStatus, 1000);
          }
        };
        $scope.checkApiStatus();


        var transform = function (data) {
            return $.param(data);
        };
        var baseURI = 'http://' + window.location.host + "/api/";
        // Modal control
        $scope.open = function (size, video) {
            var modalInstance = $modal.open({
                templateUrl: 'addModal.html',
                controller: addModalCtrl,
                size: size,
                resolve: {
                    video: function () {
                        return video;
                    },
                    added: function () {
                        return $scope.added;
                    }
                }
            });

            modalInstance.result.then(
                function () {
                }, function () {
                });
        };

        var addModalCtrl = function ($scope, $modalInstance, video, added) {
            $scope.video = video;
            $scope.password = "";
            $scope.error = false;

            $scope.addVideo = function () {
                $http.post(baseURI + 'add',
                    {
                        videoId: $scope.video.id.videoId,
                        password: $scope.password
                    },
                    {
                        headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
                        transformRequest: transform
                    }).
                    success(function (data) {
                        added.push($scope.video.id.videoId);
                        $modalInstance.close();
                    }).
                    error(function (data, status, headers, config) {
                        $scope.error = true;
                        console.error("Failed to add video");
                        console.error(status);
                    });

            };

            $scope.closeRecallModal = function () {
                $modalInstance.dismiss('cancel');
            };
        }
    }]);