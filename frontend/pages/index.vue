<template>
  <!-- Home Page -->
  <div class="techwave_fn_home">
    <div class="section_home">
      <div class="section_left">
        
        <!-- Title Shortcode -->
        <div class="techwave_fn_title_holder">
          <h1 class="title">Unlock the Bittensor Subnets</h1>
          <p class="desc">Explore and Interact with the TAO Ecosystem</p>
        </div>

        <div class="techwave_fn_interactive_list modern">
          <div v-if="!subnets" class="fn__preloader position-relative loading">
            <div class="icon"></div>
            <div class="text">Loading</div>
          </div>

          <ul>
            <li v-for="subnet in subnets" :key="subnet.id">
              <SubnetItem :subnet="subnet"
                @alert-auth="alertAuth"
              />
            </li>
          </ul>
        </div>
        
      </div>
      <div class="section_right">
        <div class="company_info">
          <img src="/img/logo-desktop-full.png" alt="">
          <p class="">Your gateway to the Bittensor subnets. Get insights, ask questions, and connect with subnet owners and stakeholders. With Bittensor, the future of decentralized AI is at your fingertips.</p>
          <hr>
          <div class="fn__members">
            <div class="active item">
              <span class="circle"></span>
              <span class="text">1694 Online</span>
            </div>
            <div class="item">
              <span class="circle"></span>
              <span class="text">77912 Members</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- !Home Page -->
</template>

<script lang="ts" setup>

import { toast } from 'vue3-toastify';
const $api = useApi()

const subnets = ref<Array<any>|null>(null)

onMounted(async () => {
  $api.get('/v1/subnets/')
    .then((response) => {
      subnets.value = response.data
    })
});

const alertAuth = () => {
  toast.error("Authorization needed.", {
    autoClose: 8000,
  })
}

</script>