<template>
	<div>
		<!-- MAIN WRAPPER -->
		<div v-if="isReadyForWork"
			class="techwave_fn_wrapper"
			:class="{ 'fn__has_sidebar': hasRightSidebar }"
		>
			<div class="techwave_fn_wrap">
			
				<Searchbar v-if="false" />

				<!-- HEADER -->
				<header class="techwave_fn_header">
				
					<!-- Header left: token information -->
					<div class="header__left">
						<TokenSummary />
					</div>
					<!-- /Header left: token information -->
					
					<!-- Header right: navigation bar -->
					<div class="header__right">
						<div class="fn__nav_bar">
							
							<HeaderActions v-if="false" />
							
							<UserBar v-if="currentAccount" />
							<SignInBar v-else />
							
						</div>
					</div>
					<!-- !Header right: navigation bar -->
					
				</header>
				<!-- !HEADER -->
				
				
				<Sidebar />
				
				<div class="techwave_fn_content">
				
					<div class="techwave_fn_page">

						<NuxtPage v-if="!isLoginRequired"/>
						<h3 v-else class="text-center mt-30px">Authorization required!</h3>
					</div>
					
					<LayoutFooter />
					
				</div>
				
			</div>
		</div>
		<div v-else class="techwave_fn_preloader enabled">
			<svg>
				<circle class="first_circle" cx="50%" cy="50%" r="110"></circle>
				<circle class="second_circle" cx="50%" cy="50%" r="110"></circle>
			</svg>
		</div>

	</div>
</template>

<script lang="ts">
	import Searchbar from '~/components/header/Searchbar.vue'
	import TokenSummary from '~/components/header/TokenSummary.vue'
	import HeaderActions from '~/components/header/HeaderActions.vue'
	import UserBar from '~/components/header/UserBar.vue'
	import Sidebar from '~/components/sidebar/Sidebar.vue'
	import LayoutFooter from '~/components/LayoutFooter.vue'
	import SignInBar from '~/components/header/SignInBar.vue'
	import { useUserStore } from "~/store"
	import { useRoute } from 'vue-router'
	import 'vue3-toastify/dist/index.css'

	const $store = useUserStore()

	export default {
		setup () {
			const route = useRoute()
			const currentRouteName = computed(() => route.name)
			return { currentRouteName }
		},
    components: {
			Searchbar,
			TokenSummary,
			HeaderActions,
			UserBar,
			Sidebar,
			LayoutFooter,
			SignInBar,
    },
		data() {
			return {
				isReadyForWork: false
			}
		},
		computed: {
			currentAccount() {
				return $store.currentAccount
			},
			hasRightSidebar() {
				const routeName = this.currentRouteName as string
				return ['subnet-slug'].includes(routeName)
			},
			isLoginRequired() {
				const routeName = this.currentRouteName as string
				return !$store.currentAccount && ['subnet-slug'].includes(routeName)
			}
		},
		async mounted() {
			const token = localStorage.getItem('token')
			if (!token) {
				this.isReadyForWork = true
			} else {
				const account = await $store.loginByToken()
				if (!account) {
					localStorage.setItem('token', '')
					console.log('Clean old token...')
				}
				this.isReadyForWork = true
		}
	}
}
</script>
