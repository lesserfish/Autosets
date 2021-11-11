<script>
    import ListItem from "./ListItem.svelte"
    import Filters from "./Filters.svelte"
    export let AppObjects;
    export let TemplateList;
    
    class ExerciseEntry{
        constructor(MuscleGroups, ExerciseTypes, Equipments, Experience)
        {
            this.MuscleGroups = MuscleGroups;
            this.ExerciseTypes = ExerciseTypes;
            this.Equipments = Equipments;
            this.Experience = Experience;
        };
    };
    
    function RemoveFromList(id)
    {
        TemplateList.splice(id, 1);
        TemplateList = TemplateList;
    }
    function RepeatEntry(id)
    {
        var entry = TemplateList[id];
        TemplateList.push(entry);
        TemplateList = TemplateList;
    }
    function AddToList(ChosenMuscles, ChosenEquipment, ChosenDifficulty, ChosenTypes)
    {
        let entry = new ExerciseEntry(ChosenMuscles, ChosenTypes, ChosenEquipment, ChosenDifficulty); 
        TemplateList.push(entry);
        TemplateList = TemplateList;
    }

</script>

<div class="row">
    <div class="col scrollSpecial">
        <p class="btn-outline-secondary disabled" data-bs-toggle="tooltip" data-bs-placement="top" title="For each exercise you wish to add to your workout, you can filter out muscle group, difficulty, required equipment and exercise type.">Add filters:</p>
        <ul class="list-group list-group-flush">

            {#each TemplateList as template, i}
                <li class="list-group-item bg-transparent liSpecial">
                    <ListItem id={i} content={template} close_function={RemoveFromList} repeat_function={RepeatEntry}/>
                </li>
            {/each}
            <li class ="list-group-item bg-transparent liSpecial">
                <button class="btn btn-outline-secondary col text-primary" data-bs-toggle="modal" data-bs-target="#FilterModal">Add</button>
            </li>
        </ul>
    </div>
</div>

<Filters bind:AppObjects={AppObjects} StoreFunction={AddToList}/>

<style>
    .liSpecial{
        border:0 !important;
    }
    .scrollSpecial{
        overflow-y: auto;
        max-height: 65vh;
    }
</style>