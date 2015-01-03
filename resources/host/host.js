$.onRocumentReady(function(){
    var tag = document.createElement('script');
    tag.src = "https://www.youtube.com/player_api";
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
    
    // Replace the 'ytplayer' element with an <iframe> and
    // YouTube player after the API code downloads.
    var player;
    var params = {
        autoplay: 1,
        modestBranding: 1,
        color: 'white'
    }
    function onYouTubePlayerAPIReady() {
    player = new YT.Player('ytplayer', {
        height: '720',
        width: '1280',
        videoId: 'M7lc1UVf-VE',
        playerVars: params
    });
    }
})