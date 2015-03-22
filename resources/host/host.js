
// 2. This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
var player;
function onYouTubeIframeAPIReady() {
    player = new YT.Player('ytplayer', {
        height: '900',
        width: '1600',
        events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
        }
    });
}

// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {
    getNext();
}

// 5. The API calls this function when the player's state changes.
//    The function indicates that when playing a video (state=1),
//    the player should play for six seconds and then stop.
function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.ENDED) {
        getNext();
    }
}
function getNext() {
    $.get( "api/next", function( data ){
        player.loadVideoById(data);
        player.playVideo();
    }).fail(function() {
        setTimeout(function(){ getNext() }, 3000);
    });
}

function ajaxNext(){

}

function stopVideo() {
    player.stopVideo();
}

var socket;
function initializeSocket(){
    socket = new WebSocket('ws://'+window.location.host+'/host/websocket');

    socket.onmessage = function(evt){
        console.log(evt.data);
        $( "#password" ).text(evt.data);
    };

    socket.onclose = function(){
        setTimeout(function(){ initializeSocket() }, 3000);
    };
}

initializeSocket();
