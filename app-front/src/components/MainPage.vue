<template>
  <div class="container">
    <div class="row align-items-start">
      <div class="col" style="width: 10rem">
        <div class="card col-lg-6 mb-4" style="width: 18rem">
          <div class="card-body">
            <div class="d-flex flex-column align-items-center text-center">
              <img
                :src="
                user.image_link
                ? user.image_link
                : 'https://bootdey.com/img/Content/avatar/avatar7.png'
                "
                alt="No Photo Available"
                class="rounded-circle"
                width="150"
              />
              <div class="mt-3">
                <h4>{{ user.fullname }}</h4>
                <p class="text-secondary mb-1" @click="goToProfile" >@{{ user.handle }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-9">
  <div class="d-flex align-items-center">
    <i class="fa-solid fa-newspaper fa-3x mr-3"></i>
    <h2 class="mb-0">NewsFeed</h2>
  </div>
  <p>News content goes here</p>
</div>

      <div class="row">
        <h2>Articles</h2>
        <div v-for="article in articles" :key="article.id">
          <div name="card4" class="card col-sm-6 offset-sm-3 lg-6 mb-4">
            <div class="post-block">
              <div class="d-flex justify-content-between">
                <div class="d-flex mb-3">
                  <div class="mr-2">
                    <a href="#!" class="text-dark"
                      ><img src="../assets/icons8-helo-48.png" alt="User" class="author-img"
                    /></a>
                  </div>
                  <div>
                    <h5 class="mb-0">
                      <a href="#!" class="text-dark">{{article.author_handle}}</a>
                    </h5>
                    <p class="mb-0 text-muted">{{article.date}}</p>
                  </div>
                </div>
              </div>
              <div class="post-block__content mb-2">
                <h6>
                  {{article.title}}
                </h6>
                <p>{{ article.body }}</p>
                <img src="../assets/icons8-helo-48.png" alt="Content img" />
              </div>
              <div class="mb-3">
                <div class="d-flex align-items-center">
                  <a class="text-danger mr-2" @click="likeArticle(article.id)">
                    <span>
                      <i class="fa fa-heart"></i>
                    </span>
                  </a>
                  <p class="mb-0 mx -2 px-1">{{ article.likes }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.sidebar {
  color: #fff !important;
  width: 280px;
  background-color: RGBA(33, 37, 41, var(--bs-bg-opacity, 1)) !important;
}
.post-block {
  padding: 20px;
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.1);
}
.fa-newspaper {
  font-size: 4rem;
}

h2 {
  font-weight: bold;
}

.author-img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
}

.text-dark {
  color: #212529;
}

.text-secondary {
  color: #6c757d;
}

.fa-heart {
  font-size: 1.2rem;
}
</style>



<script>
import axios from "axios";

export default {
  data() {
    return {
      user: {
        username: "",
        fullname: "",
        handle: "",
      },
    };
  },
  methods:{
    
      likeArticle(articleId) {
      const token = localStorage.getItem('access_token');
      if (token) {
        axios.post(`http://localhost:7000/articles/${articleId}/like`, null, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
          .then(response => {
            const index = this.articles.findIndex(article => article.id === articleId);
            this.articles[index].likes = response.data.likes;
          })
          .catch(error => {
            console.log(error);
          });
      }
    },
    
    goToProfile() {
      this.$router.push('/profile');
    }

  },
  
  mounted() {
    const token = localStorage.getItem("access_token");
    if (token) {
      axios
        .get("http://localhost:7000/get_profile", {
          headers: { Authorization: `Bearer ${token}` },
        })
        .then((response) => {
          this.user = response.data;
          console.log(response.data)
        })
        .catch((error) => {
          console.log(error);
        });
    }
    if (token){
      axios
        .get("http://localhost:7000/get_all_articles", {
         
        })
        .then((response) => {
          this.articles = response.data;
        })
        .catch((error) => {
          console.log(error);
        });

    }
  },
  
};
</script>
    

 