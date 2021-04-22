<script>
    import MediaQuery from './MediaQuery.svelte';
</script>
<style lang="scss"> 
    .wrapper {
        @include flexitem(1, 0, 100%);
        @include flexbox($align-perp: stretch);
    }
    .left, .right {
        @include flexitem(1, 0, 20%);
    }
    .pad {           
        @include flexitem(0, 1, min(600px, 20%));
    }    
    .center {
        order: 2;
        @include flexitem(1, 0, 60%); 
    }
</style>
<div class="wrapper">
    <MediaQuery query="(min-width: 600px)">  
        <div style="order: 1" class="left" class:pad={!$$slots.left}>
            <slot name="left"><div/></slot>
        </div>
        <div style="order: 3" class="right" class:pad={!$$slots.right}>
            <slot name="right"><div/></slot>
        </div>
    </MediaQuery>
    <div class="center">
        <slot name="center"/>
    </div>
</div>