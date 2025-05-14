<!-- API-Test -->
<script>
import axios from 'axios';

export default {
  name: 'ApiTest',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {

          console.error(error);
        });
    },
    
  },
  created() {
    this.getMessage();
  },
};
</script>


<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>
