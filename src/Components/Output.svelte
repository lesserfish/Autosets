<script>
import { onMount } from "svelte";
import ExerciseItem from "./ExerciseItem.svelte"

    export let AppObjects;
    export let TemplateList;
    export let ExerciseList;
    
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
            }
            if(AcceptableWorkouts.length > 0)
            {
                let idx = Math.floor(Math.random()* AcceptableWorkouts.length);
                let exercise = AcceptableWorkouts[idx];
                ExerciseList.push(exercise)
            }
        }
        finished = true;
    }

    onMount(async () => {
        ExerciseList = []
        FillExerciseList();
    });
</script>

<div class="row">
    <div class="col scrollSpecial">
        <p class="btn-outline-secondary disabled" data-bs-toggle="tooltip" data-bs-placement="top" title="For each exercise you wish to add to your workout, you can filter out muscle group, difficulty, required equipment and exercise type.">Add filters:</p>
        <ul class="list-group list-group-flush">

            {#each ExerciseList as exercise, i}
                <li class="list-group-item bg-transparent liSpecial">
                    <ExerciseItem ExerciseEntry={exercise} id={i} AppObjects={AppObjects} template={TemplateList[i]}/>
                </li>
            {/each}
        </ul>
    </div>
</div>

