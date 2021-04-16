<script>
    import Module from './Module.svelte';
    let innerWidth = 0;
    let innerHeight = 0;
    
    let orientation = "landscape";
    $: orientation = innerWidth >= innerHeight ? "landscape" : "portrait";
</script>

<svelte:window bind:innerWidth={innerWidth} bind:innerHeight={innerHeight}/>

{#if orientation=="landscape"}
<div class="grid-desktop">
    <Module title="Calendar" desc="no events. no life." version=1 />    
    <Module title="Expenses" desc="no money." version=1 />    
    <Module title="Lights" desc="no lights." version=1 />    
    <Module title="Linux" desc="i use arch btw." version=1 />    
    <Module title="Todo" desc="nothing todo." version=1 />    
</div>
{:else}
<div class="flex-mobile">
    <Module title="Calendar" desc="no events. no life." version=1 mobile=true />    
    <Module title="Expenses" desc="no money." version=1 mobile=true />    
    <Module title="Lights" desc="no lights." version=1 mobile=true />    
    <Module title="Linux" desc="i use arch btw." version=1 mobile=true />    
    <Module title="Todo" desc="nothing todo." version=1 mobile=true />    
</div>
{/if}


<style lang="scss">

    .grid-desktop {
        width: 100%;

        @media screen and (min-width: 0px) {
            margin-top: $gap;
            @include infinite-grid($row-size: 23rem, $columns: repeat(1, 34rem), $grid-gap: $gap);
        }

        @media screen and (min-width: 800px) {
            margin-top: $gap * 3;
            @include infinite-grid($row-size: 23rem, $columns: repeat(2, 34rem), $grid-gap: $gap);
        }        
        @media screen and (min-width: 1600px) {
            @include infinite-grid($row-size: 23rem, $columns: repeat(3, 34rem), $grid-gap: $gap);
        }
    }

    .flex-mobile {
        width: 100%;
        padding: 0 $gap;
        margin-top: $gap;
        @include flexbox($direction: column, $align-main: flex-start, $align-perp: stretch, $align-content: flex-start);   
    }

    

</style>