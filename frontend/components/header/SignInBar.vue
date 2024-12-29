<template>
  <!-- User (bar item) -->
  <div class="bar__item bar__item_user" :class="{ 'opened': isOpened }">
    <a @click.stop="isOpened = !isOpened" class="techwave_fn_button cursor-pointer"><span>Sign In</span></a>
    <NuxtLink to="/signup"
      class="techwave_fn_button ml-10px"
    >
      <span>Sign Up</span>
    </NuxtLink>
    <div class="item_popup">
      <div class="sign__content">
        <form id="login-form"
          class="login"
          method="POST"
          @submit.native.prevent="submitLogin"
        >
          <div class="form__content">
            <div class="form__title">Sign In</div>
            
            <div class="form__username mb-20px">
              <label for="user_login">Usern email</label>
              <input type="text"
                v-model="loginForm.email"
                :disabled="isProcessing"
                class="input w-full submit-item"
                id="id_username"
                name="username"
                autocapitalize="off"
                autocomplete="username"
                aria-describedby="login-message"
                required
              >
            </div>

            <div class="form__pass mb-20px">
              <div class="pass_lab">
                <label for="user_password">Password</label>
                <a href="#">Forget Password?</a>
              </div>
              <input type="password"
                v-model="loginForm.password"
                :disabled="isProcessing"
                class="input w-full submit-item"
                id="id_password"
                name="password"
                autocomplete="current-password"
                required
                spellcheck="false"
              >
            </div>

            <div class="form__submit mb-20px">
              <label class="fn__submit">
                <input type="submit"
                  name="submit"
                  value="Sign In"
                  class="submit-item"
                  :disabled="isProcessing"
                >
              </label>
            </div>
          </div>
        </form>
        <div class="sign__desc">
          <p>Not a member? <NuxtLink to="/signup">Sign Up</NuxtLink></p>
        </div>
      </div>


    </div>
  </div>
  <!-- !User (bar item) -->
</template>

<script lang="ts" setup>

import { useUserStore } from "~/store"

const $store = useUserStore()
const $api = useApi()

const isOpened = ref(false)
const isProcessing = ref(false)

const loginForm = ref({
  email: '',
  password: ''
})

const submitLogin = async () => {
  isProcessing.value = true

  await $api.post(`/auth/jwt/create/`, loginForm.value)
    .then((response) => {
      localStorage.setItem('token', response.data.access)
      localStorage.setItem('refresh', response.data.refresh)
    })
    .catch((error) => {
      isProcessing.value = false
      console.log('Auth error', error)
      alert('Auth error')
    })
  await $store.loginByToken()
  isProcessing.value = false
}

</script>
