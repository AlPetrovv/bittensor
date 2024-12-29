<template>
  <!-- User (bar item) -->
  <div class="bar__item bar__item_user" :class="{ 'opened': isOpened }">
    <a @click.stop="isOpened = !isOpened" class="user_opener cursor-pointer">
      <img src="/img/user/user.png" alt="">
    </a>
    <div class="item_popup">
      <div class="user_profile">
        <div class="user_img">
          <img src="/img/user/user.png" alt="">
        </div>
        <div class="user_info">
          <h2 class="user_name">{{accountName}}<span>Free</span></h2>
          <p>{{ accountEmail }}</p>
        </div>
      </div>
      <div class="user_nav">
        <ul>
          <!-- <li>
            <a href="user-profile.html">
              <span class="icon"><img src="/svg/person.svg" alt="" class="fn__svg"></span>
              <span class="text">Profile</span>
            </a>
          </li>
          <li>
            <a href="user-settings.html">
              <span class="icon"><img src="/svg/setting.svg" alt="" class="fn__svg"></span>
              <span class="text">Settings</span>
            </a>
          </li>
          <li>
            <a href="user-billing.html">
              <span class="icon"><img src="/svg/billing.svg" alt="" class="fn__svg"></span>
              <span class="text">Billing</span>
            </a>
          </li> -->
          <li>
            <a @click="logout" class="cursor-pointer">
              <span class="icon"><img src="/svg/logout.svg" alt="" class="fn__svg"></span>
              <span class="text">Log Out</span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
  <!-- !User (bar item) -->
</template>

<script lang="ts" setup>
	import { useUserStore } from "~/store"
	const $store = useUserStore()
  const isOpened = ref(false)

  const currentAccount = computed(() => {
    return $store.currentAccount
  })

  const accountEmail = computed(() => {
    return currentAccount.value.email
  })

  const accountName = computed(() => {
    return accountEmail.value.includes('@') ? accountEmail.value.split('@')[0] : accountEmail.value
  })

  const logout = () => {
    localStorage.removeItem('token')
    $store.logout()
  }

</script>