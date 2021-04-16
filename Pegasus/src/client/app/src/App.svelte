<script>
  import Nav from "./components/main/Nav.svelte";
  import Runtime from "./components/main/Runtime.svelte";
  import Logo from "./components/main/Logo.svelte";
  import ModulesGrid from "./components/main/ModulesGrid.svelte";

  let width;
</script>

<svelte:window bind:innerWidth={ width }></svelte:window>
<main class="main-page-wrapper">
  <nav class="top-content-wrapper">
    <div class="pad" />
    <div class="main-content">
      {#if width > 900}
      <Logo class="logo ts-1 bold t-2" />
      {/if}
      <Nav />
      {#if width > 900}
      <Runtime uptime={3}/>
      {/if}
    </div>
    <div class="pad" />
    <div class="accent-line" />
  </nav>
  <div class="main-content-wrapper">
    <div class="main-content-left" />
      <ModulesGrid />
    <div class="main-content-right" />
  </div>
</main>

<style lang="scss">
  :global(*) {
    margin: 0;
    box-sizing: border-box;
  }
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
  :global(body) {		
	height: auto;
    padding: 0;	
  }

  .main-page-wrapper {
	padding-bottom: $gap;
    width: 100%;
    min-height: 100vh;
    background: $dark;
    @include flexbox($direction: column, $align-perp: stretch);

    .top-content-wrapper {
      position: relative;
      background: $darker;

      @include shadow(#000000, 0.4, 0.5rem, 1rem, 1.5rem, 0.7rem);
      @include flexitem(0, 0, $top-bar-sizing);
      @include flexbox(row, nowrap, flex-start, stretch, flex-start);

      .main-content {
        @include flexitem(1, 1, 50%);
        @include flexbox(row, nowrap, flex-start, center, flex-start);
      }

      .accent-line {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 3px;

        background: linear-gradient(to right, $accent, $base);
      }

      .pad {
        @include flexitem(1, 1, 25%);
      }
    }
  }
</style>
