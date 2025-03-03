let menu_logo=document.querySelector(".menu-logo-js");
let videos_info=document.querySelector(".videos-info-js");
let main_video=document.querySelector(".main_video");

menu_logo.addEventListener("click", ()=>{
  if(videos_info.style.display=="none")
  {
    videos_info.style.display="flex";

  }
  else{
    videos_info.style.display="none";
    main_video.style.width="70%";
  }
});

