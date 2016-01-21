(() => {
    "use strict";
    /* Video Cover */
    scaleVideoContainer();

    initBannerVideoSize('.Hero-wrapper .Hero-filter');
    initBannerVideoSize('.Hero-wrapper .Hero-video');

    $(window).on('resize', () => {
        scaleVideoContainer();
        scaleBannerVideoSize('.Hero-wrapper .Hero-filter');
        scaleBannerVideoSize('.Hero-wrapper .Hero-video');
    });


    function scaleVideoContainer() {

        let height = $(window).height();
        let unitHeight = parseInt(height) + 'px';
        $('.Hero').css('height',unitHeight);

    }

    function initBannerVideoSize(element){

        $(element).each(function(){
            $(this).data('height', $(this).height());
            $(this).data('width', $(this).width());
        });

        scaleBannerVideoSize(element);
    }

    function scaleBannerVideoSize(element){

        let windowWidth = $(window).width();
        let windowHeight = $(window).height() + 5;
        let videoWidth;
        let videoHeight;

        $(element).each(function(){
            let videoAspectRatio = $(this).data('height')/$(this).data('width');

            $(this).width(windowWidth);

            if(windowWidth < 1000){
                videoHeight = windowHeight;
                videoWidth = videoHeight / videoAspectRatio;
                $(this).css({'margin-top' : 0, 'margin-left' : -(videoWidth - windowWidth) / 2 + 'px'});

                $(this).width(videoWidth).height(videoHeight);
            }

            $('.Hero .Hero-wrapper .Hero-video').addClass('fadeIn animated');

        });
    }
    /* End Video Cover */

    /* View more link */
        $('.ViewMore').on('click', function() {
            console.log('Click me....')
            $(document.body).animate({
                'scrollTop': $('.Education').offset().top
            }, 1000)
        })
    /* End View more link */

})();
