<template>
  <li class="group__item">
    <div class="fn__chat_link"
      :class="{'active': isActive, 'opened': isOpened, 'live_edit': isEdit}"
      @click="$emit('select', chat)"
    >
      <span class="text">{{ chat.name }}</span>
      <input type="text" v-model="newName" @keypress.enter="saveChat">
      <span class="options">
        <button class="trigger" @click.stop="isOpened = !isOpened"><span></span></button>
        <span class="options__popup">
          <span class="options__list">
            <button class="edit" @click="openEdit">Edit</button>
            <button class="delete" @click="$emit('remove-chat', chat)">Delete</button>
          </span>
        </span>
      </span>
      <span class="save_options">
        <button class="save" @click="saveChat">
          <img src="/svg/check.svg" alt="" class="fn__svg">
        </button>
        <button class="cancel" @click="isEdit=false">
          <img src="/svg/close.svg" alt="" class="fn__svg">
        </button>
      </span>
    </div>
  </li>
</template>

<script lang="ts" setup>

  import api from "~/plugins/api";
import { useUserStore } from "~/store"

  const $emit = defineEmits()
  const $api = useApi()
  const $store = useUserStore()

  const $props = defineProps({
    chat: {
      type: Object,
      required: true
    },
    isActive: {
      type: Boolean,
      default: false
    },
  })

  const isOpened = ref(false)
  const isEdit = ref(false)
  const newName = ref('')

  const openEdit = () => {
    newName.value = $props.chat.name
    isEdit.value = true
  }

  const saveChat = () => {
    const chatId = $props.chat.id
    $api.patch(`/v1/chats/${chatId}/`, { name: newName.value })
      .then(() => {
        $emit('update-name', newName.value)
        isEdit.value = false
      })
  }

  document.body.addEventListener('click', () => isOpened.value = false)

</script>