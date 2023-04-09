<template>
    <div>
      <h2>Articles</h2>
      <ul>
        <li v-for="article in articles" :key="article.id">
          <h3>{{ article.title }}</h3>
          <p>{{ article.body }}</p>
          <p>Author: {{ article.author_id }}</p>
          <p>Date: {{ article.date }}</p>
          <p>Likes: {{ article.likes }}</p>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        articles: [],
      };
    },
    mounted() {
      axios
        .get("loaclhost:7000/get_articles")
        .then((response) => {
          this.articles = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  };
  </script>
  