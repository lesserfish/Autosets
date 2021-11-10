<script>
    export let value = 0;
</script>


<div class="row">
    <div class="col">
        Template with value {value}
    </div>
</div>

<div class="row">
    <div class="col-4"></div>
    <div class="col">
        <div class="btn-group" role="group">
            <button type="button" class="btn btn-outline-secondary shadow-sm" on:click={() => {value--;}}> - </button>
            <button type="button" class="btn btn-lg btn-outline-secondary disabled">                </button>
            <button type="button" class="btn btn-outline-secondary shadow-sm" on:click={() => {value++;}}> + </button>
        </div>
    </div>
    <div class="col-4"></div>
</div>	

<style>
</style>