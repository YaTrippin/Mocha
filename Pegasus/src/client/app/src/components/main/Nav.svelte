<div class="nav-group">
    <a class="item ts-2 t-4">Dashboard</a>
    <a class="item ts-2 t-4">Modules</a>
    <a class="item ts-2 t-4">System</a>
</div>

<style type="text/scss">
    // @import '../../../sass/_mixins.scss';

    .nav-group {
        @include flexitem(1, 1, auto);
        @include flexbox(row, nowrap, center, center, flex-start);
        
        .item {
            cursor: pointer;
            text-decoration: none;
            display: inline-block;

            &:not(:last-child) {
                margin-right: 5ch;
            }

            &:hover {
                color: $accent;
            }
        }
    }
</style>