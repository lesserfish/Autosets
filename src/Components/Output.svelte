<script>
import { onMount } from "svelte";
import ExerciseItem from "./ExerciseItem.svelte"

    export let AppObjects;
    export let TemplateList;
    export let ExerciseList;
    
    let ExerciseIndexList = [];

    let save_message = "";
    let finished = false;

    class ExerciseEntry{
        constructor(MuscleGroups, ExerciseTypes, Equipments, Experience)
        {
            this.MuscleGroups = MuscleGroups;
            this.ExerciseTypes = ExerciseTypes;
            this.Equipments = Equipments;
            this.Experience = Experience;
        };
    };


    async function FillExerciseList(){
        for(let i = 0; i < TemplateList.length; i++)
        {
            let AcceptableWorkouts = [];
            let AcceptableWorkoutsIndex = [];
            let template = TemplateList[i];
            
            for(let j = 1; j <= Object.values(AppObjects.workoutObject).length; j++)
            {
                let workout = AppObjects.workoutObject[j];

                let workout_musclegroup = workout["MuscleGroup"];
                let workout_equipment = workout["Equipment"];
                let workout_experience = workout["Experience"];
                let workout_types = workout["Type"];

                if(template.MuscleGroups.indexOf(workout_musclegroup) == -1){
                    continue;
                }
                if(template.ExerciseTypes.indexOf(workout_types) == -1){
                    continue;
                }
                if(template.Equipments.indexOf(workout_equipment) == -1){
                    continue;
                }
                if(template.Experience.indexOf(workout_experience) == -1){
                    continue;
                } 
                AcceptableWorkouts.push(workout);
                AcceptableWorkoutsIndex.push(j);
            }
            if(AcceptableWorkouts.length > 0)
            {
                let idx = Math.floor(Math.random()* AcceptableWorkouts.length);
                let exercise = AcceptableWorkouts[idx];
                ExerciseList.push(exercise)
                ExerciseIndexList.push(AcceptableWorkoutsIndex[idx]);
            }
        }

        finished = true;
    }

    onMount(async () => {
        ExerciseList = []
        FillExerciseList();
    });
        function SaveToCookie()
        {
            if(ExerciseIndexList.length == 0){
                save_message = "There is nothing to save."
                let myModal = new bootstrap.Modal(document.getElementById('exampleModal'));
                myModal.toggle();
                return;
            }
            let i = 0;
            while(true)
            {
                let cookie_name = "workout" + String(i);
                if(!document.cookie.split(';').some( (item) => item.trim().startsWith(cookie_name + "=")))
                {
                    console.log("Creating cookie with name: " + cookie_name);
                    
                    let cookie_value = "";
                    for(let k = 0; k < ExerciseIndexList.length; k++)
                    {
                        cookie_value += ExerciseIndexList[k]+",";
                    }
                    cookie_value = cookie_value.substr(0, cookie_value.length - 1);

                    let cookie = cookie_name+"="+cookie_value + "; SameSite=Lax";
                    document.cookie = cookie;
                    save_message = "Workout was saved to cookies."
                    let myModal = new bootstrap.Modal(document.getElementById('exampleModal'));
                    myModal.toggle();
                    return;
                }
                i = i + 1;
            }

        }
</script>

<div class="row">
    <div class="col scrollSpecial">
        <p class="btn-outline-secondary disabled" data-bs-toggle="tooltip" data-bs-placement="top" title="For each exercise you wish to add to your workout, you can filter out muscle group, difficulty, required equipment and exercise type.">Your results:</p>
        <ul class="list-group list-group-flush">

            {#each ExerciseList as exercise, i}
                <li class="list-group-item bg-transparent liSpecial">
                    <ExerciseItem ExerciseEntry={exercise} ExerciseIndex={ExerciseIndexList[i]} id={i} AppObjects={AppObjects} template={TemplateList[i]}/>
                </li>
            {/each}
            <li class ="list-group-item bg-transparent liSpecial">
                <button class="btn btn-outline-secondary col-1 text-primary" on:click={SaveToCookie}>Save</button>
            </li>
        </ul>
    </div>
</div>

<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-body">
        <p>{save_message}.</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>

<style>
    .liSpecial{
        border:0 !important;
    }
    .scrollSpecial{
        overflow-y: auto;
        max-height: 75vh;
    }
</style>