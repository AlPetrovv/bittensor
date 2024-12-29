<template>
  <!-- AI Chat Bot Page -->
  <div class="techwave_fn_aichatbot_page fn__chatbot">

    <div v-if="!currentSubnet" class="fn__preloader position-relative loading mt-auto">
      <div class="icon"></div>
      <div class="text">Loading</div>
    </div>

    <div v-if="currentSubnet" class="chat__page">
    
      <div class="font__trigger">
        <span></span>
      </div>
      
      <Chat v-if="currentChat"
        :title="currentChat.name"
        :dialog="currentDialog"
        :is-checking-updates="isCheckingUpdates"
        @reload-chat="loadDialog()"
      />
      
      <div class="chat__comment">
        <div class="container">
          <div class="fn__chat_comment">
            <div class="new__chat">
              <p>Learn, ask, and discuss with Subnet 2: Omron.</p>
            </div>
            <!-- <textarea rows="1" class="fn__hidden_textarea" tabindex="-1"></textarea> -->
            <textarea rows="1" v-if="currentChat"
              placeholder="Send a message..."
              v-model="currentChat.my_message"
              :disabled="isSendProcessing"
              @keypress.enter="sendMessage"
            ></textarea>
            <button :disabled="!currentChat || !currentChat.my_message || !currentChat.my_message.length || isSendProcessing"
              :class="{ 'bg-white': currentChat && currentChat.my_message && currentChat.my_message.length && !isSendProcessing }"
              @click="sendMessage"
            >
              <img src="/svg/enter.svg" alt="" class="fn__svg">
            </button>
          </div>
        </div>
      </div>
      
    </div>
    
    <div class="chat__sidebar">
      <div class="sidebar_header">
        <a @click="createChat" class="fn__new_chat_link cursor-pointer">
          <span class="icon"></span>
          <span class="text">New Chat</span>
        </a>

      </div>
      <div v-if="currentSubnet" class="sidebar_content">

        <div class="chat__group new">
          <h2 class="group__title">Chats list:</h2>
          <ul v-if="subnetChats" class="group__list">
            <ChatSideItem v-for="chat in subnetChats"
              :key="chat.id"
              :chat="chat"
              :is-active="currentChat && currentChat.id == chat.id"
              @select="currentChat=chat"
              @update-name="chat.name = $event"
              @remove-chat="removeChat"
            />
          </ul>
        </div>
      </div>
    </div>
    
  </div>
  <!-- !AI Chat Bot Page -->
</template>

<script lang="ts" setup>
import Chat from '~/components/subnet/chat/Chat.vue'
import ChatSideItem from '~/components/subnet/chat/ChatSideItem.vue'
import api from '~/plugins/api';
import { useUserStore } from "~/store"

const $api = useApi()
const $route = useRoute()
const slug = $route.params.slug
const $store = useUserStore()

const isSendProcessing = ref(false)
const subnets = ref<Array<any>|null>(null)
const currentSubnet = ref<any|null>(null)
const subnetChats = ref<Array<any>|null>(null)
const currentChat = ref<any|null>(null)
const currentDialog = ref<any|null>(null)
const maximumAnswerId = ref(0)
const isCheckingUpdates = ref(false)

const loadTotal = async () => {

  subnets.value = null
  currentSubnet.value = null
  subnetChats.value = null
  currentChat.value = null
  currentDialog.value = null


  await $api.get('/v1/subnets/')
    .then((response) => {
      subnets.value = response.data
      currentSubnet.value = response.data.find((x: any) => x.slug == slug)
      console.log('currentSubnet.value', currentSubnet.value)
    })
  await $api.get(`/v1/subnets/${slug}/chats/`)
    .then((response) => {
      subnetChats.value = response.data
      response.data.forEach((chat: any) => {
        chat.my_message = ''
      });
      if (subnetChats.value?.length) {
        currentChat.value = subnetChats.value[0]
      }
    })

}

onMounted(async () => {
  await loadTotal()
  loadDialog()
})

const loadDialog = () => {
  currentDialog.value = null
  if (!currentChat.value) {
    return
  }
  $api.get(`/v1/chats/${currentChat.value.id}/messages/`)
    .then((response) => {
      currentDialog.value = response.data
      maximumAnswerId.value = getMaximumAnswerId(response.data.messages)
      setTimeout(() => {
        const scrollArea = document.querySelector('html') as HTMLElement
        scrollArea.scrollTop = scrollArea.scrollHeight
      }, 200);
    })
}

const createChat = () => {
  const newChat = {
    name: 'New Chat',
    user: $store.currentAccount.id,
    subnet: currentSubnet.value.id
  }
  $api.post(`/v1/chats/`, newChat)
    .then((response) => {
      if (subnetChats.value) {
        subnetChats.value.push(response.data)
        currentChat.value = subnetChats.value[subnetChats.value?.length - 1]
      }
    })
}

const removeChat = (chat: any) => {
  if (confirm('Are you sure to remove this chat?')) {
    $api.delete(`/v1/chats/${chat.id}/`, chat)
      .then(() => {
        loadTotal()
      })
  }
}

const sendMessage = () => {
  if (!currentChat.value || !currentChat.value.my_message) {
    return
  }
  isSendProcessing.value = true
  $api.post('/v1/question/', {
    text: currentChat.value.my_message,
    chat: currentChat.value.id,
    user: $store.currentAccount.id
  }).then((response: any) => {
    if (currentDialog.value && currentDialog.value.messages) {
      currentDialog.value.messages.push(response.data)
      isSendProcessing.value = false
      currentChat.value.my_message = ''
    }
  })
  .catch(() => {
    isSendProcessing.value = false
    alert('Sending error')
  })
}

const getMaximumAnswerId = (messages: Array<any>) => {
  let localMaximumId = 0
  for(let i=0; i< messages.length; i++) {
    const message = messages[i]
    for(let l=0; l< message.answers.length; l++) {
      const answer = message.answers[l]
      if (answer.id > localMaximumId) {
        localMaximumId = answer.id
      }
    }
  }
  return localMaximumId
}

// TODO: !
const culcNeedReload = async () => {
  if (!currentChat.value) {
    return false
  }
  let messages = null as null|Array<any>
  await $api.get(`/v1/chats/${currentChat.value.id}/messages/`)
    .then((response) => {
      messages = response.data.messages
    })

  if (!messages) {
    return false
  }
  const localMaximumId = getMaximumAnswerId(messages)
  if (localMaximumId > maximumAnswerId.value) {
    maximumAnswerId.value = localMaximumId
    return true
  }
  return false
}

watch(() => currentChat.value, () => {
  loadDialog()
})

setInterval(async () => {
  isCheckingUpdates.value = true
  const needUpdate = await culcNeedReload()
  if (needUpdate) {
    loadDialog()
  }
  isCheckingUpdates.value = false
}, 10000)

</script>
