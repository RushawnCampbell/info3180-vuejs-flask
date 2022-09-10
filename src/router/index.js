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
            path: '/mainresult',
            name: 'mainresult',
            component: () =>
                import ('../views/MainResultView.vue')
        },

        {
            path: '/singleresult/:recid',
            name: 'singleresult',
            component: () =>
                import ('../views/SingleResultView.vue')
        },
        {
            path: '/adminhub',
            name: 'adminhub',
            component: () =>
                import ('../views/AdminView.vue')
        },
        {
            path: '/singlemod/:recid',
            name: 'singlemod',
            component: () =>
                import ('../views/SingleModView.vue')
        },
    ]
})

export default router