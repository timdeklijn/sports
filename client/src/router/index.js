import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Exercises from '../components/Exercises.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
	{
		path: '/exercises',
		name: 'Exercises',
		component: Exercises
	},
]

const router = new VueRouter({
  routes
})

export default router
