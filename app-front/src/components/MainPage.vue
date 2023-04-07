<template>
  <div class="container">
    <div class="row align-items-start">
      <div class="col" style="width: 10rem">
        <div class="card col-lg-6 mb-4" style="width: 18rem">
          <div class="card-body">
            <div class="d-flex flex-column align-items-center text-center">
              <img
                src="https://bootdey.com/img/Content/avatar/avatar7.png"
                alt="No Photo Available"
                class="rounded-circle"
                width="100"
              />
              <div class="mt-3">
                <h4>{{ user.name }}</h4>
                <p class="text-secondary mb-1">@johndoe21</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-9">
        <p>NewsFeed</p>
        <i class="fa-solid fa-newspaper"></i>
        second card
      </div>
      <div class="row">
        <div name="card1" class=" card col-sm-6 offset-sm-3 lg-6 mb-4">
          <div class="post-block">
            <div class="d-flex justify-content-between">
              <div class="d-flex mb-3">
                <div class="mr-2">
                  <a href="#!" class="text-dark"
                    ><img src="img/user1.jpg" alt="User" class="author-img"
                  /></a>
                </div>
                <div>
                  <h5 class="mb-0">
                    <a href="#!" class="text-dark">Kiran Acharya</a>
                  </h5>
                  <p class="mb-0 text-muted">5m ago</p>
                </div>
              </div>
            </div>
            <div class="post-block__content mb-2">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Ratione laboriosam non atque, porro cupiditate commodi?
                Provident culpa vel sit enim!
              </p>
              <img src="img/food1.jpg" alt="Content img" />
            </div>
            <div class="mb3">
                <div class="d-flex">
                                <a href="#!" class="text-danger mr-2"><span><i class="fa fa-heart"></i></span></a>
                                <!-- <a href="#!" class="text-dark mr-2"><span>Comment</span></a> -->
                                <p class="mb-0">Liked by 5</p>
                    
                            </div>
            </div>
          </div>
        </div>
        <div name="card2" class=" card col-sm-6 offset-sm-3 lg-6 mb-4">
          <div class="post-block">
            <div class="d-flex justify-content-between">
              <div class="d-flex mb-3">
                <div class="mr-2">
                  <a href="#!" class="text-dark"
                    ><img src="img/user1.jpg" alt="User" class="author-img"
                  /></a>
                </div>
                <div>
                  <h5 class="mb-0">
                    <a href="#!" class="text-dark">Kiran Acharya</a>
                  </h5>
                  <p class="mb-0 text-muted">5m ago</p>
                </div>
              </div>
            </div>
            <div class="post-block__content mb-2">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Ratione laboriosam non atque, porro cupiditate commodi?
                Provident culpa vel sit enim!
              </p>
              <img src="img/food1.jpg" alt="Content img" />
            </div>
            <div class="mb3">
                <div class="d-flex">
                                <a href="#!" class="text-danger mr-2"><span><i class="fa fa-heart"></i></span></a>
                                <!-- <a href="#!" class="text-dark mr-2"><span>Comment</span></a> -->
                                <p class="mb-0">Liked by 5</p>
                    
                            </div>
            </div>
          </div>
        </div>
        <div name="card3" class=" card col-sm-6 offset-sm-3 lg-6 mb-4">
          <div class="post-block">
            <div class="d-flex justify-content-between">
              <div class="d-flex mb-3">
                <div class="mr-2">
                  <a href="#!" class="text-dark"
                    ><img src="img/user1.jpg" alt="User" class="author-img"
                  /></a>
                </div>
                <div>
                  <h5 class="mb-0">
                    <a href="#!" class="text-dark">Kiran Acharya</a>
                  </h5>
                  <p class="mb-0 text-muted">5m ago</p>
                </div>
              </div>
            </div>
            <div class="post-block__content mb-2">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Ratione laboriosam non atque, porro cupiditate commodi?
                Provident culpa vel sit enim!
              </p>
              <img src="img/food1.jpg" alt="Content img" />
            </div>
            <div class="mb3">
                <div class="d-flex">
                                <a href="#!" class="text-danger mr-2"><span><i class="fa fa-heart"></i></span></a>
                                <!-- <a href="#!" class="text-dark mr-2"><span>Comment</span></a> -->
                                <p class="mb-0">Liked by 5</p>
                    
                            </div>
            </div>
          </div>
        </div>
        <div name="card4" class=" card col-sm-6 offset-sm-3 lg-6 mb-4">
          <div class="post-block">
            <div class="d-flex justify-content-between">
              <div class="d-flex mb-3">
                <div class="mr-2">
                  <a href="#!" class="text-dark"
                    ><img src="img/user1.jpg" alt="User" class="author-img"
                  /></a>
                </div>
                <div>
                  <h5 class="mb-0">
                    <a href="#!" class="text-dark">Kiran Acharya</a>
                  </h5>
                  <p class="mb-0 text-muted">5m ago</p>
                </div>
              </div>
            </div>
            <div class="post-block__content mb-2">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Ratione laboriosam non atque, porro cupiditate commodi?
                Provident culpa vel sit enim!
              </p>
              <img src="img/food1.jpg" alt="Content img" />
            </div>
            <div class="mb3">
                <div class="d-flex">
                                <a href="#!" class="text-danger mr-2"><span><i class="fa fa-heart"></i></span></a>
                                <!-- <a href="#!" class="text-dark mr-2"><span>Comment</span></a> -->
                                <p class="mb-0">Liked by 5</p>
                    
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
</style>
<script>
export default {
  data() {
    return {
      user: {
        name: "John Doe",
        email: "johndoe@example.com",
      },
    };
  },
};
</script>
    


