<script>
    export let value = 0;
    let saved_content = ""
    function SaveCookie()
    {
        console.log(document);
        document.cookie = "value=" + String(value)+ "; SameSite=lax; Secure;path=/";
    }
    function PrintCookie()
    {
        saved_content = document.cookie;
    }

</script>


<div class="container">
    <div class="row">
        <p>Value square equals {value * value}</p>
    </div>
    <div class="row-6 sparse">
			<button type="button" class="btn btn-outline-secondary shadow-sm" on:click={SaveCookie}> Save </button> 
    </div>
    <div class="row-6 sparse">
			<button type="button" class="btn btn-outline-secondary shadow-sm" on:click={PrintCookie}> Print </button> 
    </div>
    {#if saved_content != ""}
        <div class="row sparse">
            <p>{saved_content}</p> 
        </div>
    {/if}
</div>

<style>
    .sparse{
        margin-top: 2%;
        margin-bottom: 2%;
    }
</style>