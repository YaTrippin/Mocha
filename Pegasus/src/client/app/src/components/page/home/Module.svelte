<script>
    export let name;
    export let version;
    export let desc;
    export let mobile = false;
</script>

<style lang="scss">
    card {
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

        &:not(.mobile) .title {
            font-size: 3.3rem;
        }
        &:not(.mobile) .content {
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
    }
    .mobile {
        @include flexitem(0, 0, 8rem);
        @include flexbox($align-main: space-between, $align-perp: flex);
        margin-top: 2rem;
        .title {
            font-size: 2.5rem;
        }
    }
</style>

{#if mobile}
    <card class="mobile">
        <span class="title medium">{name}</span>
        <span class="ts-2 t-3">{version != 0 ? `v${version}` : ''}</span>
    </card>
{:else}
<card>
    <div class="title medium">{name}<span class="ts-2 t-4">{version != 0 ? ` v${version}` : ' '} <span></div>
    <p class="content ts-4 medium">{desc}</p>
</card>
{/if}