import { createRouter, createWebHashHistory } from "vue-router";
// import ListArticles from "./components/ListArticles.vue"
import CreateArticles from "./components/CreateArticles.vue"
import MainPage from "./components/MainPage.vue"
import ListFollowers from "./components/ListFollowers.vue"
import ProfileView from "./components/ProfileView.vue"
import LoginPage from "./components/LoginPage.vue"
import SignUp from "./components/SignUp.vue"
import testpage from "./components/StartingPage.vue"
const routes=[
    {
        path: "/",
        name:"login",
        component:LoginPage,
    },
    {
        path: "/signup",
        name:"signup",
        component:SignUp,
    },
    {
        path: "/test",
        name:"test",
        component:testpage,
    },
    {
        path: "/home",
        name:"home",
        component:MainPage,
        beforeEnter: (to, from, next) => {
            const accessToken = localStorage.getItem('access_token')
            if (accessToken) {
              next()
            } else {
              next('/')
            }
          }
    },
    {
        path:"/create",
        name:"create",
        component:CreateArticles,
        beforeEnter: (to, from, next) => {
            const accessToken = localStorage.getItem('access_token')
            if (accessToken) {
              next()
            } else {
              next('/')
            }
          }
    },
    {
        path:"/followers",
        name:"followers",
        component:ListFollowers,
        beforeEnter: (to, from, next) => {
            const accessToken = localStorage.getItem('access_token')
            if (accessToken) {
              next()
            } else {
              next('/')
            }
          }
    },
    {
        path:"/profile",
        name:"profile",
        component:ProfileView,
        beforeEnter: (to, from, next) => {
            const accessToken = localStorage.getItem('access_token')
            if (accessToken) {
              next()
            } else {
              next('/')
            }
          }
    }
]

const router = createRouter({
    history:createWebHashHistory(),
    routes,
})

export default router;