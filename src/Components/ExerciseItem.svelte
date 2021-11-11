<script>
  import { onMount } from "svelte";

  export let AppObjects;
  export let ExerciseEntry;
  export let ExerciseIndex;
  export let id;
  export let template;

  function ReplaceEntry() {
    let AcceptableWorkouts = [];
    let AcceptableWorkoutsIndex = [];

    for (let j = 1; j <= Object.values(AppObjects.workoutObject).length; j++) {
      let workout = AppObjects.workoutObject[j];

      let workout_musclegroup = workout["MuscleGroup"];
      let workout_equipment = workout["Equipment"];
      let workout_experience = workout["Experience"];
      let workout_types = workout["Type"];

      if (template.MuscleGroups.indexOf(workout_musclegroup) == -1) {
        continue;
      }
      if (template.ExerciseTypes.indexOf(workout_types) == -1) {
        continue;
      }
      if (template.Equipments.indexOf(workout_equipment) == -1) {
        continue;
      }
      if (template.Experience.indexOf(workout_experience) == -1) {
        continue;
      }
      AcceptableWorkouts.push(workout);
      AcceptableWorkoutsIndex.push(j);
    }
    if (AcceptableWorkouts.length > 0) {
      let idx = Math.floor(Math.random() * AcceptableWorkouts.length);
      let exercise = AcceptableWorkouts[idx];
      ExerciseEntry = exercise;
      ExerciseIndex = AcceptableWorkoutsIndex[idx];
    }
  }
</script>

<a
  class="btn btn-outline-secondary col-8 text-left textSpecial"
  data-bs-toggle="collapse"
  href="#collapseLink{id}"
  role="button"
  aria-expanded="false"
  aria-controls="collapseExample"
>
  {ExerciseEntry["Name"]}
</a>
<button
  class="btn bi-arrow-repeat col"
  type="button"
  style="font-size:130%"
  on:click={ReplaceEntry}
/>
<a
  href={ExerciseEntry["Link"]}
  class="link-primary"
  target="_blank"
  rel="noopener noreferrer"
>
  Link
</a>

<div class="collapse" id="collapseLink{id}">
  <div class="card card-body bg-transparent cardSpecial">
    <b> Muscle groups:</b>
    <p>{ExerciseEntry["MuscleGroup"]}</p>
    <b> Equipment:</b>
    <p>{ExerciseEntry["Equipment"]}</p>
    <b> Difficulty:</b>
    <p>{ExerciseEntry["Experience"]}</p>
    <b> Exercise Type:</b>
    <p>{ExerciseEntry["Type"]}</p>
  </div>
</div>

<style>
  .cardSpecial {
    border: 0 !important;
    padding-bottom: 0 !important;
    padding-top: 10px;
  }
  .cardSpecial > p {
    margin: 0;
  }
  .textSpecial {
    text-align: left;
  }
</style>
