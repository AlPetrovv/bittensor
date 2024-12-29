<template>
  <div class="item">
    <NuxtLink v-if="isAuthorize" :to="'/subnet/' + subnet.slug">
      <span class="icon">
        <img :src="iconUrl" alt="" class="fn__svg">
      </span>
      <h2 class="title">SN {{ subnet.number }}: {{ subnet.name }}</h2>
      <span class="arrow"><img src="/svg/arrow.svg" alt="" class="fn__svg"></span>
    </NuxtLink>
    <a v-else @click="$emit('alert-auth')">
      <span class="icon">
        <img :src="iconUrl" alt="" class="fn__svg">
      </span>
      <h2 class="title">SN {{ subnet.number }}: {{ subnet.name }}</h2>
      <span class="arrow"><img src="/svg/arrow.svg" alt="" class="fn__svg"></span>
    </a>
  </div>
</template>

<script>

  import { useUserStore } from "~/store"
	
  export default {
    setup () {
			const store = useUserStore()
			return { store }
		},
    props: {
      subnet: {
        type: Object,
        required: true
      },
      iconUrl: {
        type: String,
        default: '/svg/chat.svg'
      },
    },
    computed: {
      isAuthorize() {
        return !!this.store.currentAccount
      }
    }
  }

</script>