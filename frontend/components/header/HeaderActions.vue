<template>
  <!-- Search (bar item) -->
    <div class="bar__item bar__item_search">
    <a href="#" class="item_opener">
      <img src="/svg/search.svg" alt="" class="fn__svg">
    </a>
    <div class="item_popup">
      <input type="text" placeholder="Search">
    </div>
  </div>
  <!-- !Search (bar item) -->
  
  <!-- Notification (bar item) -->
  <div class="bar__item bar__item_notification has_notification">
    <a href="#" class="item_opener">
      <img src="/svg/bell.svg" alt="" class="fn__svg">
    </a>
    <div class="item_popup">
      <div class="ntfc_header">
        <h2 class="ntfc_title">Notifications</h2>
        <a>View All</a>
      </div>
      <div class="ntfc_list">
        <ul>
          <li>
            <p><a>Version 4.1.2 has been launched</a></p>
            <span>34 Min Ago</span>
          </li>
          <li>
            <p><a>Video Generation has been released</a></p>
            <span>12 Apr</span>
          </li>
          <li>
            <p><a>Terms has been updated</a></p>
            <span>12 Apr</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
  <!-- !Notification (bar item) -->
  
  <!-- Full Screen (bar item) -->
  <div class="bar__item bar__item_fullscreen">
    <a href="#" class="item_opener">
      <img src="/svg/fullscreen.svg" alt="" class="fn__svg f_screen">
      <img src="/svg/smallscreen.svg" alt="" class="fn__svg s_screen">
    </a>
  </div>
  <!-- !Full Screen (bar item) -->
  
  <!-- Language (bar item) -->
  <div class="bar__item bar__item_language">
    <a href="#" class="item_opener">
      <img src="/svg/language.svg" alt="" class="fn__svg">
    </a>
    <div class="item_popup">
      <ul>
        <li>
          <span class="active">English</span>
        </li>
        <li>
          <a href="#">Spanish</a>
        </li>
        <li>
          <a href="#">French</a>
        </li>
      </ul>
    </div>
  </div>
  <!-- !Language (bar item) -->
  
  <!-- Site Skin (bar item) -->
  <div class="bar__item bar__item_skin">
    <a href="#" class="item_opener">
      <img src="/svg/sun.svg" alt="" class="fn__svg light_mode">
      <img src="/svg/moon.svg" alt="" class="fn__svg dark_mode">
    </a>
    <div class="item_popup">
      
    </div>
  </div>
  <!-- !Site Skin (bar item) -->
</template>