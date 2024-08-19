<template>
  <q-page class="flex flex-center">
    <h1>{{ data.message }}</h1>
  </q-page>
</template>

<script setup>

import { ref, onMounted } from 'vue'
import axios from 'axios'
const data = ref({ message: 'Hello World' })

onMounted(async () => {
  await axios('http://localhost:8000/api')
    .then(res => { data.value = res.data })
    .catch((err) => { data.value = err; console.log(err) })
})

</script>
