import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
    history: createWebHistory(
        import.meta.env.BASE_URL),
    routes: [{
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/about',
            name: 'about',
            component: () =>
                import ('../views/AboutView.vue')
        },

        {
            path: '/signin',
            name: 'signin',
            component: () =>
                import ('../views/SigninView.vue')

        },

        {
            path: '/signout',
            name: 'signout',
            component: () =>
                import ('../views/SignoutView.vue')

        },

        {
            path: '/signup',
            name: 'signup',
            component: () =>
                import ('../views/SignupView.vue')
        },

        {
            path: '/search',
            name: 'search',
            component: () =>
                import ('../views/SearchView.vue')
        },

        {
            path: '/singleresult',
            name: 'singleresult',
            component: () =>
                import ('../views/SingleresView.vue')
        }
    ]
})

export default router