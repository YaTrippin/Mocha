<script>
    import Module from './Module.svelte';
    import MediaQuery from '../../layout/MediaQuery.svelte';
    
    let modules = [
        { name: "Calendar", version: "0", desc: "yet another calendar"},
        { name: "Todos", version: "1", desc: "there's nothing todo"},
        { name: "Lights", version: "2", desc: "it's still dark here"},
        { name: "Linux", version: "2", desc: "i use arch btw"}
    ]
</script>

<style lang="scss">
    grid {
        @media screen and (min-width: 600px) {
            margin-top: 3 * $gap;
            @include infinite-grid($row-size: 23rem, $columns: repeat(2, 34rem), $grid-gap: $gap);
        }
        @media screen and (min-width: 1440px) {
            margin-top: 2 * $gap;
            @include infinite-grid($row-size: 23rem, $columns: repeat(3, 34rem), $grid-gap: $gap);
        }
    }
    flexlist {
        padding: $gap;
        @include flexbox($direction: column, $align-perp: stretch);
    }
</style>
<MediaQuery query="(max-width: 599px)">
    <flexlist>
        {#each modules as module}
            <Module {...module} mobile=true/>
        {/each}
    </flexlist>
</MediaQuery>
<MediaQuery query="(min-width: 600px)">
    <grid>
        {#each modules as module}
            <Module {...module}/>
        {/each}
    </grid>
</MediaQuery>