<template>
  <div class="container" style="max-width: none">
    <div>
      <SplitGrid class="sb_split-grid" direction="row">
        <!--<SplitGridArea>-->
          <!--<button type="button" class="btn btn-primary" v-for="menu in menus" :key="menu"-->
            <!--v-on:click="getPrettyJson">-->
            <!--{{ menu.menuType }}-->
          <!--</button>-->
        <!--</SplitGridArea>-->
        <SplitGrid class="sb_sub-grid">
          <SplitGridArea>
            <div>
              <textarea v-model="originalJson" style="resize: none; width: 100%" rows="25"
                        v-on:keyup="getPrettyJson">

              </textarea>
            </div>
          </SplitGridArea>
          <SplitGridGutter/>
          <SplitGridArea>
            <json-viewer
            :value="jsonData"
            :expand-depth=10
            copyable
            expanded></json-viewer>
          </SplitGridArea>
        </SplitGrid>
        <!--<SplitGridGutter/>-->
      </SplitGrid>
    </div>

    <!--<div style="width: 100%">-->
      <!--<p>vue-json-editor</p>-->
      <!--<vue-json-editor v-model="json" :show-btns="true" :expandedOnStart="true"-->
                       <!--@json-change="onJsonChange"></vue-json-editor>-->
    <!--</div>-->

  </div>
</template>

<script>
import axios from 'axios';
import JsonViewer from 'vue-json-viewer';
// import vueJsonEditor from 'vue-json-editor';
import { SplitGrid, SplitGridArea, SplitGridGutter } from 'vue-split-grid';

export default {
  name: 'JsonDisplay',
  data() {
    return {
      menus: null,
      prettyJson: null,
      originalJson: null,
      jsonData: null,
    };
  },
  components: {
    JsonViewer,
    // vueJsonEditor,
    SplitGrid,
    SplitGridArea,
    SplitGridGutter,
  },
  methods: {
    onJsonChange(value) {
      console.log('value:', value);
    },
    getMenus() {
      const path = 'http://localhost:5000/menus';
      axios
        .get(path)
        .then((res) => {
          console.log(res);
          this.menus = res.data.result;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getPrettyJson(event) {
      console.log(event);
      console.log(this.originalJson);
      const path = 'http://localhost:5000/json';
      axios
        .put(path, {
          original_json: this.originalJson,
          operate_type: 'pretty',
        })
        .then((res) => {
          if (res.data.code === 200) {
            this.jsonData = res.data.result;
          } else {
            this.jsonData = res.data.message;
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getPrettyJson();
    this.getMenus();
  },
};
</script>

<style>
  /*body {*/
    /*margin: 0;*/
  /*}*/

  /*.container {*/
    /*font-family: "Avenir", Helvetica, Arial, sans-serif;*/
    /*-webkit-font-smoothing: antialiased;*/
    /*-moz-osx-font-smoothing: grayscale;*/
    /*text-align: center;*/
    /*color: #2c3e50;*/
    /*height: 100vh;*/
    /*overflow: hidden;*/
  /*}*/

  /*.sb_split-grid {*/
    /*height: 100%;*/
    /*width: 100%;*/
  /*}*/

  /*body, html, #app {*/
    /*min-height: 100%;*/
    /*width: 100%;*/
  /*}*/
</style>

<style scoped>

</style>
