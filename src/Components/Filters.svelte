<script>
import { onMount } from "svelte";


    export let AppObjects;
    let ChosenMuscles = [];
    let ChosenEquipment = [];
    let ChosenDifficulty = [];
    let ChosenTypes = [];
    export let StoreFunction;
    
    function checkAll(all_id, check_id_array)
    {
        if(document.getElementById(all_id).checked)
        {
            if(all_id == "allMuscles"){
                ChosenMuscles = [];
                for(let i = 0; i < check_id_array.length; i++)
                {
                    ChosenMuscles.push(check_id_array[i]);
                }
            }
            if(all_id == "allEquipment"){
                ChosenEquipment = [];
                for(let i = 0; i < check_id_array.length; i++)
                {
                    ChosenEquipment.push(check_id_array[i]);
                }
            }
            if(all_id == "allDifficulty"){
                ChosenDifficulty = [];
                for(let i = 0; i < check_id_array.length; i++)
                {
                    ChosenDifficulty.push(check_id_array[i]);
                }
            }
            if(all_id == "allTypes"){
                ChosenTypes = [];
                for(let i = 0; i < check_id_array.length; i++)
                {
                    ChosenTypes.push(check_id_array[i]);
                }
            }
        }
        else{

            if(all_id == "allMuscles"){
                ChosenMuscles = [];
            }
            if(all_id == "allEquipment"){
                ChosenEquipment = [];
            }
            if(all_id == "allDifficulty"){
                ChosenDifficulty = [];
            }
            if(all_id == "allTypes"){
                ChosenTypes = [];
            }
        }
    }

    function FillEmpty()
    {

            if(ChosenMuscles.length == 0){
                for(let i = 0; i < Object.values(AppObjects.muscleGroupArray).length; i++)
                {
                    ChosenMuscles.push(Object.values(AppObjects.muscleGroupArray)[i]);
                }
            }
            if(ChosenEquipment.length == 0){
                for(let i = 0; i <  Object.values(AppObjects.equipmentArray).length; i++)
                {
                    ChosenEquipment.push(Object.values(AppObjects.equipmentArray)[i]);
                }
            }
            if(ChosenDifficulty.length == 0){
                for(let i = 0; i <  Object.values(AppObjects.experienceArray).length; i++)
                {
                    ChosenDifficulty.push(Object.values(AppObjects.experienceArray)[i]);
                }
            }
            if(ChosenTypes.length == 0)
            {
                for(let i = 0; i < Object.values(AppObjects.exerciseTypeArray).length; i++)
                {
                    ChosenTypes.push(Object.values(AppObjects.exerciseTypeArray)[i]);
                }
            }
            ChosenMuscles = ChosenMuscles;
            ChosenEquipment = ChosenEquipment;
            ChosenDifficulty = ChosenDifficulty;
            ChosenTypes = ChosenTypes;
    }

    onMount(() => {
        FillEmpty();
    });
</script>

<div class="modal fade" id="FilterModal" tabindex="-1" aria-labelledby="ModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Select your filters:</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">

        <div class="accordion accordion-flush" id="FilterAccordionFlush">

            <div class="accordion-item">

                <h2 class="accordion-header" id="flush-headingOne">
                          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#Muscle-collapse" aria-expanded="false" aria-controls="flush-collapseOne">
                                Muscle Groups:  
                          </button>
                </h2>

            </div>
            <div id="Muscle-collapse" class="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#FilterAccordionFlush">
                        <div class="accordion-body">
                            
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" id="allMuscles" on:change={() => {checkAll("allMuscles", Object.values(AppObjects.muscleGroupArray));}} checked>
                                <label class="form-check-label" for="muscle-group-1"> All </label>
                            </div>
                            {#each Object.values(AppObjects.muscleGroupArray) as muscleGroup, i}
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" value="{muscleGroup}" id="{muscleGroup}" bind:group={ChosenMuscles}>
                                <label class="form-check-label" for={muscleGroup}> {muscleGroup}</label>
                            </div>
                            {/each}
                        </div>
            </div>

            <div class="accordion-item">

                <h2 class="accordion-header" id="flush-headingOne">
                          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#Equipment-Collapse" aria-expanded="false" aria-controls="flush-collapseOne">
                                Equipment:  
                          </button>
                </h2>

            </div>
            <div id="Equipment-Collapse" class="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#FilterAccordionFlush">
                        <div class="accordion-body">
                            
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" id="allEquipment" on:change={() => {checkAll("allEquipment", Object.values(AppObjects.equipmentArray));}} checked>
                                <label class="form-check-label" for="muscle-group-1"> All </label>
                            </div>
                            {#each Object.values(AppObjects.equipmentArray) as equipment, i}
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" value="{equipment}" id="{equipment}" bind:group={ChosenEquipment}>
                                <label class="form-check-label" for={equipment}> {equipment}</label>
                            </div>
                            {/each}
                        </div>
            </div>
            <div class="accordion-item">

                <h2 class="accordion-header" id="flush-headingOne">
                          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#Difficulty-Collapse" aria-expanded="false" aria-controls="flush-collapseOne">
                                Difficulty:  
                          </button>
                </h2>

            </div>
            <div id="Difficulty-Collapse" class="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#FilterAccordionFlush">
                        <div class="accordion-body">
                            
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" id="allDifficulty" on:change={() => {checkAll("allDifficulty", Object.values(AppObjects.experienceArray));}} checked>
                                <label class="form-check-label" for="muscle-group-1"> All </label>
                            </div>
                            {#each Object.values(AppObjects.experienceArray) as difficulty, i}
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" value="{difficulty}" id="{difficulty}" bind:group={ChosenDifficulty}>
                                <label class="form-check-label" for={difficulty}> {difficulty}</label>
                            </div>
                            {/each}
                        </div>
            </div>
            <div class="accordion-item">

                <h2 class="accordion-header" id="flush-headingOne">
                          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#Type-Collapse" aria-expanded="false" aria-controls="flush-collapseOne">
                                Exercise Type:  
                          </button>
                </h2>

            </div>
            <div id="Type-Collapse" class="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#FilterAccordionFlush">
                        <div class="accordion-body">
                            
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" id="allTypes" on:change={() => {checkAll("allTypes", Object.values(AppObjects.exerciseTypeArray));}} checked>
                                <label class="form-check-label" for="muscle-group-1"> All </label>
                            </div>
                            {#each Object.values(AppObjects.exerciseTypeArray) as etype, i}
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" value="{etype}" id="{etype}" bind:group={ChosenTypes}>
                                <label class="form-check-label" for={etype}> {etype}</label>
                            </div>
                            {/each}
                        </div>
            </div>

        </div>


      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-outline-primary" on:click={() => {StoreFunction(ChosenMuscles, ChosenEquipment, ChosenDifficulty, ChosenTypes)}}>Add</button>
      </div>
    </div>
  </div>
</div>

<style>
    .modal{
        overflow-y: auto;
    }
</style>