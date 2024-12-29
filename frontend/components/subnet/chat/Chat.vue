<template>
  <div class="fn__title_holder">
    <div class="container">
      <!-- Active chat title -->
      <h1 class="title">{{ title }}</h1>
      <small v-if="isCheckingUpdates" style="position: absolute;right: 13px;top: 37px;">Checking updates...</small>
      <button v-else class="cursor-pointer"
        style="position: absolute;right: 13px;top: 37px;"
        @click="$emit('reload-chat')"
      >
        <img src="/svg/regenerate.svg" alt="" class="fn__svg">
      </button>

      <!-- !Active chat title -->
    </div>
  </div>

  <div class="container">

    <div v-if="dialog" class="chat__list">

      <div class="chat__item active" >
        <template v-for="message in dialog.messages">
          <div class="chat__box your__chat">
            <div class="author"><span>You</span></div>
            <div class="chat">
              <p>{{ message.text }}</p>
            </div>
          </div>
          <div v-for="answer in message.answers" class="chat__box bot__chat">
            <div class="author"><span>{{dialog.subnet}}</span></div>
            <div class="chat">
              <p>{{ answer.text }}</p>
            </div>
          </div>
        </template>
      </div>
    </div>
    <div v-else class="fn__preloader position-relative loading mt-auto">
      <div class="icon"></div>
      <div class="text">Loading</div>
    </div>

  </div>

</template>

<script lang="ts" setup>

  const $props = defineProps({
    title: {
      type: String,
      required: true
    },
    dialog: {
      type: Object as () => any|null,
      default: null
    },
    isCheckingUpdates: {
      type: Boolean,
      default: false
    }
  })

</script>