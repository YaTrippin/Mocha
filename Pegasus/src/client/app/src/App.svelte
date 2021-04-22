<script>
  import { Router, Route } from "svelte-navigator";

  import MainContent from "./components/layout/MainContent.svelte"
  import MediaQuery from "./components/layout/MediaQuery.svelte";
  import Home from "./components/page/home/Home.svelte";
  import TopBar from "./components/global/TopBar.svelte";
  
  let showTopBar = true;
</script>

<style lang='scss'>
  :global(html) {
    @media screen and (min-width: 0px) {
      font-size: 6px;
    }
    @media screen and (min-width: 900px) {
      font-size: 8px;
    }
    @media screen and (min-width: 1400px) {
      font-size: 9px;
    }
    @media screen and (min-width: 2200px) {
      font-size: 10px;
    }
    
	  @include scrollbegone();
  }

  :global(*) {
    padding: 0;
    margin: 0;
  }

  page {
    min-height: 100vh;
    width: 100%;
    background: $dark;    
    @include flexbox($direction: column, $align-perp: stretch);    
  }
  
</style>

<page>

  <Router primary={false}>
    {#if showTopBar}
      <TopBar></TopBar>
    {/if}
    <Route path="/" component={Home}/>
  </Router>
</page>