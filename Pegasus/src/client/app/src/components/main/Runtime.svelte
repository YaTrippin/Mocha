<script>
    export let uptime
</script>

<div class="ts-1 t-4 medium this">
    { uptime } { uptime == 1 ? "hour" : "hours"}
</div>

<style lang="scss">
    // @import '../../../sass/app.scss';

    .this {        
        @include flexitem(0, 0, 10ch);
        text-align: right;
    }
    
</style>