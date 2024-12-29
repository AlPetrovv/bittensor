import { defineStore } from 'pinia'
const $api = useApi()

export const useUserStore = defineStore('user', {
  state: () => ({
    account: null as any|null
  }),
  getters: {
    currentAccount: (state: any) => state.account
  },
  actions: {
    async loginByToken() {
      await $api.get('/v1/users/me/')
        .then((response: any) => {
          this.account = response.data
        })
        .catch(() => {
          this.account = null
        })
        return this.account
    },
    logout() {
      this.account = null
    }
  },
})