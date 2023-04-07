import { createRouter, createWebHashHistory } from "vue-router";
// import ListArticles from "./components/ListArticles.vue"
import CreateArticles from "./components/CreateArticles.vue"
import MainPage from "./components/MainPage.vue"
import ListFollowers from "./components/ListFollowers.vue"
import ProfileView from "./components/ProfileView.vue"

const routes=[
    {
        path: "/",
        name:"home",
        component:MainPage,
    },
    {
        path:"/create",
        name:"create",
        component:CreateArticles,
    },
    {
        path:"/followers",
        name:"followers",
        component:ListFollowers,
    },
    {
        path:"/profile",
        name:"profile",
        component:ProfileView,
    }
]

const router = createRouter({
    history:createWebHashHistory(),
    routes,
})

export default router;