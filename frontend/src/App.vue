<script setup>
import { ref, onMounted } from 'vue';

const movies = ref([]);

const fetchMovies = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/movies/popular');
    const data = await response.json();
    movies.value = data.results; 
  } catch (error) {
    console.error("Error al traer las películas:", error);
  }
};

onMounted(fetchMovies);
</script>

<template>
  <section class="py-5">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-6">
          
          <h2 class="mb-4">Catálogo</h2>
          
          <ul class="list-group lead">
            <li v-for="(movie, index) in movies" :key="index" class="list-group-item d-flex justify-content-between align-items-center">
              {{ movie.title }}
              <span class="badge bg-secondary">{{ movie.year }}</span>
            </li>
          </ul>

        </div>
      </div>
    </div>
  </section>
</template>