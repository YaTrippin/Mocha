<script>
    export let title
    export let desc
    export let version = 0
    export let mobile = false
</script>
{#if !mobile}
<div class="wrapper">    
    <div class="title medium"> { title } <span class="ts-2 t-4">{version != 0 ? `V${ version }` : ''}</span></div>
    <p class="content ts-4 medium"> { desc } </p>
</div>
{:else}
<div class="wrapper mobile">    
    <div class="title ts-1 medium"> { title }</div>
    <p class="content ts-3 medium"> { desc } </p>
</div>
{/if}

<style lang="scss">
    // @import '../../sass/_mixins.scss';
    div.wrapper {

        padding: $card-padding;
        border-radius: $card-radius;
        
        @include shadow(#000000, 0.4, 1rem, 1rem, 1.5rem, 0.1rem);
        background: linear-gradient(to bottom, $accent 50%, $darker 50%);
        background-size: 100% 200%;
        background-position-y: 100%;
        color: $text-shade-1;
        text-align: center;
        cursor: pointer;
        transition: background-position 100ms ease-in-out 10ms,
                    box-shadow 150ms ease-in-out 20ms;

        @include scrollbegone();
        @include flexbox($align-main: center, $align-perp: center);
        
        .title {
            font-size: 3.3rem;
        }

        .content {
            display: none;
            font-size: 2rem;
        }

        &:hover, 
        &:focus {
            background-position: 0 0;
            @include shadow($accent, 0.15, 1rem, 1rem, 3rem, 0.4rem);

            .content {
                display: block;
            }

            .title {
                display: none;
            }
        }
        &.s {
            font-size: 1rem;
        }

        &.m {
            font-size: 2rem;
        }

        &.l {
            font-size: 2.4rem;
        }
    }
    div.mobile {        
        margin-top: $gap / 2;
        @include flexitem(0, 0, $gap);
        border-radius: $gap;
    }
</style>