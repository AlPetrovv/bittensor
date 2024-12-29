<template>
  <!-- Sign Up -->
  <div class="techwave_fn_sign">
    
    <div class="sign__content">
      <form id="signup-form"
        class="signup"
        method="POST"
        @submit.native.prevent="submitForm"
      >
        <div class="form__content">
          <div class="form__title">Sign Up</div>
          <!-- <div class="form__name">
            <label for="name">Name</label>
            <input type="text" class="input" id="name" placeholder="Full Name">
          </div>
          <div class="form__username">
            <label for="username">Username</label>
            <input type="text" class="input" id="username" placeholder="Username">
          </div> -->
          <div class="form__email">
            <label for="email">Username</label>
            <input v-model="loginForm.email"
              type="text"
              class="input submit-item"
              id="email"
              placeholder="yourmail@example.com"
              :disabled="isProcessing"
              required
            >
          </div>
          <div class="form__pass">
            <label for="user_password">Password</label>
            <input v-model="loginForm.password"
              type="password"
              id="user_password"
              class="submit-item"
              autocomplete="current-password"
              spellcheck="false"
              :disabled="isProcessing"
              required
            >
          </div>
          <div class="form__pass">
            <label for="user_password">Password retry</label>
            <input v-model="loginForm.re_password"
              type="password"
              id="re_password"
              class="submit-item"
              autocomplete="current-password"
              spellcheck="false"
              :disabled="isProcessing"
              required
            >
          </div>
          <div class="form__submit">
            <label class="fn__submit">
              <input type="submit"
                name="submit"
                value="Create Account"
                :disabled="isProcessing"
              >
            </label>
          </div>
          <!-- <div class="form__alternative">
            <div class="fn__lined_text">
              <div class="line"></div>
              <div class="text">Or</div>
              <div class="line"></div>
            </div>
            <a href="#" class="techwave_fn_button"><span>Sign up with Google</span></a>
          </div> -->
          <div class="sign__desc">
            <p>Back to the <NuxtLink to="/">main page</NuxtLink></p>
          </div>
        </div>
      </form>
    </div>
    
  </div>
  <!-- !Sign Up -->

</template>

<script lang="ts" setup>

  import { count } from "console";
  import { useUserStore } from "~/store"

  const $router = useRouter()
  const $store = useUserStore()
  const $api = useApi()

  const isProcessing = ref(false)

  const loginForm = ref({
    email: '',
    password: '',
    re_password: '',
  })

  const submitForm = async () => {
    isProcessing.value = true
    let newAccount = null

    await $api.post(`/v1/users/`, loginForm.value)
      .then((response) => {
        newAccount = response.data
      })
      .catch((error) => {
        isProcessing.value = false
        console.log('Register error', error)
        alert('Register error')
      })
    
    if(!newAccount) {
      return
    }

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

    const result = await $store.loginByToken()
    isProcessing.value = false

    if (result) {
      $router.push({ path: '/' })
    }
  }


</script>
