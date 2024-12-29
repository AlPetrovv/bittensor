<template>
  <!-- LEFT PANEL -->
  <div class="techwave_fn_leftpanel">
    
    <div class="mobile_extra_closer"></div>
    
    <!-- logo (left panel) -->
    <div class="leftpanel_logo">
      <NuxtLink to="/" class="fn_logo">
        <span class="full_logo">
          <img src="/img/logo-desktop-full.png" alt="" class="desktop_logo">
          <img src="/img/logo-retina-full.png" alt="" class="retina_logo">
        </span>
        <span class="short_logo">
          <img src="/img/logo-desktop-mini.png" alt="" class="desktop_logo">
          <img src="/img/logo-retina-mini.png" alt="" class="retina_logo">
        </span>
      </NuxtLink>
      <a href="#" class="fn__closer fn__icon_button desktop_closer">
        <img src="/svg/arrow.svg" alt="" class="fn__svg">
      </a>
      <a href="#" class="fn__closer fn__icon_button mobile_closer">
        <img src="/svg/arrow.svg" alt="" class="fn__svg">
      </a>
    </div>
    <!-- !logo (left panel) -->
    
    <!-- content (left panel) -->
    <div class="leftpanel_content">
    
      <!-- #1 navigation group -->
      <div class="nav_group">
        <h2 class="group__title">Start Here</h2>
        <ul class="group__list">
          <li>
            <NuxtLink to="/" class="fn__tooltip menu__item" data-position="right" title="Home">
              <span class="icon"><img src="/svg/home.svg" alt="" class="fn__svg"></span>
              <span class="text">Home</span>
            </NuxtLink>
          </li>
        </ul>
      </div>
      <!-- !#1 navigation group -->
    
      <!-- #2 navigation group -->
      <div class="nav_group">
        <h2 class="group__title">Subnets</h2>
        <ul class="group__list">
          <li v-for="(subnet, index) in subnets" :key="subnet.id">
            <NuxtLink v-if="isAuthorize" :to="'/subnet/' + subnet.slug" class="fn__tooltip menu__item" data-position="right" title="Image Generation">
              <span class="icon">
                <img :src="index == 0 ? '/svg/cube.svg' : '/svg/chat.svg'" alt="" class="fn__svg">
              </span>
              <span class="text">SN {{ subnet.number }}: {{ subnet.name }}</span>
            </NuxtLink>
            <a v-else class="fn__tooltip menu__item" data-position="right" title="Image Generation">
              <span class="icon">
                <img :src="index == 0 ? '/svg/cube.svg' : '/svg/chat.svg'" alt="" class="fn__svg">
              </span>
              <span class="text">SN {{ subnet.number }}: {{ subnet.name }}</span>
            </a>
          </li>
        </ul>
      </div>
      <!-- !#2 navigation group -->
    
      <!-- #3 navigation group -->
      <div class="nav_group">
        <h2 class="group__title">Others</h2>
        <ul class="group__list">
          <!-- <li>
            <NuxtLink to="/" class="fn__tooltip menu__item" data-position="right" title="Pricing">
              <span class="icon"><img src="/svg/dollar.svg" alt="" class="fn__svg"></span>
              <span class="text">Pricing</span>
            </NuxtLink>
          </li> -->
          <li>
            <a @click="logout" class="fn__tooltip menu__item cursor-pointer" data-position="right" title="Log Out">
              <span class="icon"><img src="/svg/logout.svg" alt="" class="fn__svg"></span>
              <span class="text">Log Out</span>
            </a>
          </li>
        </ul>
      </div>
      <!-- !#3 navigation group -->
      
      
    </div>
    <!-- !content (left panel) -->
    
  </div>
  <!-- !LEFT PANEL -->

</template>

<script lang="ts" setup>

  import { useUserStore } from "~/store"

  const $api = useApi()
	const $store = useUserStore()

  const subnets = ref<Array<any>|null>(null)

  const logout = () => {
    localStorage.removeItem('token')
    $store.logout()
  }
  const isAuthorize = computed(() => {
    return !!$store.currentAccount
  })

  onMounted(async () => {
    $api.get('/v1/subnets/')
      .then((response) => {
        subnets.value = response.data
      })
  });

</script>