<script>
    import { useNavigate } from 'svelte-navigator';
    import MediaQuery from '../layout/MediaQuery.svelte';
    import Logo from './Logo.svelte';
    
    export let forceTop = false;
    let navigate = useNavigate();
    let status = "5 Hours";
    let navLinks = [
        {name: 'Home', url: '/'},
        {name: 'System', url: '/system'},
        {name: 'Config', url: '/config'}
    ];
</script>

<style lang="scss">
    bar {
        background: $darker;

        position: relative; // For accent line
        @include shadow(#000000, 0.4, 0.5rem, 1rem, 1.5rem, 0.7rem);
        @include flexitem(0, 0, $top-bar-sizing);
        @include flexbox(row, nowrap, flex-start, center, flex-start);

        @media screen and (max-width: 599px) {
            $top-bar-sizing: 12rem;
            @include flexitem(0, 0, $top-bar-sizing);
        }
        
        .forceTop {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: $top-bar-sizing;
        }
    }

    accent {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 3px;

        background: linear-gradient(to right, $accent, $base);
    }

    .pad {
        @include flexitem(0, 1, min(600px, 20%));
    }

    navlist {
        @include flexitem(1, 0, auto);
        @include flexbox($align-main: center, $align-perp: center);
    }

    item {
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        user-select: none;

        &:not(:last-child) {
            margin-right: 5ch;
        }

        &:hover {
            color: $accent;
        }
    }

</style>

<bar class:forceTop={ forceTop }>
    <MediaQuery query="(min-width: 900px)">
        <div class="pad" style="order: 1"/>
        <Logo styleProp="order: 2"/>
        <navlist style="order: 3">
            {#each navLinks as link} 
                <item class="item ts-2 t-4" on:click="{() => navigate(link.url)}">{link.name}</item>
            {/each}
        </navlist>
        <status class="ts-1 t-4 medium" style="order: 4">{status}</status>        
        <div class="pad" style="order: 5">
    </MediaQuery>
    
    <accent/>
</bar>