<script>
    import { onMount } from "svelte";
    import * as WorkoutJSON  from "../JSON/Workout.json"
    export let AppObjects = {
        workoutObject : [],
        muscleGroupArray : [],
        exerciseTypeArray : [],
        equipmentArray : [],
        experienceArray : [],
    };


    onMount(async () => {

        AppObjects.workoutObject = WorkoutJSON.Exercises;

        for(let i = 0; i < AppObjects.workoutObject.length; i++)
        {
            var currentObject = AppObjects.workoutObject[i];

            if(AppObjects.muscleGroupArray.indexOf(currentObject.MuscleGroup) == -1){
                AppObjects.muscleGroupArray.push(currentObject.MuscleGroup);
            }
            if(AppObjects.exerciseTypeArray.indexOf(currentObject.ExerciseType) == -1){
                AppObjects.exerciseTypeArray.push(currentObject.ExerciseType);
            }        
            if(AppObjects.equipmentArray.indexOf(currentObject.Equipment) == -1){
                AppObjects.equipmentArray.push(currentObject.Equipment);
            }
            if(AppObjects.experienceArray.indexOf(currentObject.Experience) == -1){
                AppObjects.experienceArray.push(currentObject.Experience);
            }

        }
        console.log("Length: " + AppObjects.muscleGroupArray.length);
    });
</script>


<!--
<ul>
	List of Exercises:
	{#each AppObjects.workoutObject as wo}
	<li>
			{wo.Name} <br>
	</li>
	{/each}
</ul>
<ul>
	List of Muscle Groups:
	{#each AppObjects.muscleGroupArray as mg}
	<li>
			{mg} <br>
	</li>
	{/each}
</ul>
<ul>
	List of Equipment:
	{#each AppObjects.equipmentArray as eq}
	<li>
			{eq} <br>
	</li>
	{/each}
</ul>
<ul>
	List of Experience:
	{#each AppObjects.experienceArray as ex}
	<li>
			{ex} <br>
	</li>
	{/each}
</ul>
<ul>
	List of Exercises:
	{#each AppObjects.exerciseTypeArray as et}
	<li>
			{et} <br>
	</li>
	{/each}
</ul>

-->