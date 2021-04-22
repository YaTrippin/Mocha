<script>
    import { onMount } from 'svelte';
    
    export let query;
    let mql;
    let matchedQuery;

    onMount(() => {
        mql = window.matchMedia(query);

        matchedQuery = mql.matches; // Updates matchedQuery onload

        let listener = (mql) => {
            matchedQuery = mql.matches;
        }

        mql.addListener(listener);
        return () => { mql.removeListener(listener)};   // Remove listener on unmount
    });
</script>

{#if matchedQuery}
    <slot />
{/if}