<script>
    import ListItem from "./ListItem.svelte"
    export let AppObjects;
    export let TemplateList;

    function RemoveFromList(id)
    {
        TemplateList.splice(id, 1);
        TemplateList = TemplateList;
    }
</script>


<div class="row">
    <div class="col">
        <p> Add execises:</p>
        <ul class="list-group list-group-flush">

            {#each TemplateList as template, i}
                <li class="list-group-item bg-transparent liSpecial">
                    <ListItem id={i} content={template} close_function={RemoveFromList}/>
                </li>
            {/each}
            <li class ="list-group-item bg-transparent liSpecial">
                <button class="btn btn-outline-secondary col-1 text-primary">Add</button>
            </li>
        </ul>
    </div>
</div>

<div class="container">


</div>
<style>
    .liSpecial{
        border:0 !important;
    }
</style>