<script>
  import { onMount } from "svelte";
  import ExerciseItem from "./ExerciseItem.svelte";
  import { fade, fly } from "svelte/transition";

  export let AppObjects;
  export let saved_cookies = [];

  let ExerciseList = [];
  let ExerciseIndexList = [];

  let TemplateList = [];

  onMount(() => {
    console.log(document.cookie);
    let i = 0;
    while (true) {
      let cookie_name = "workout" + String(i);
      if (
        !document.cookie
          .split(";")
          .some((item) => item.trim().startsWith(cookie_name + "="))
      ) {
        saved_cookies = saved_cookies;
        return;
      }
      saved_cookies.push(cookie_name);
      i = i + 1;
    }
  });
  function LoadExerciseList(i) {
    ExerciseIndexList = [];
    ExerciseList = [];

    let cookie_name = "workout" + String(i);
    const cookie_value = document.cookie
      .split("; ")
      .find((row) => row.startsWith(cookie_name + "="))
      .split("=")[1];
    let exercises = cookie_value.split(",");
    for (let i = 0; i < exercises.length; i++) {
      let exercise_id = exercises[i];
      ExerciseIndexList.push(exercise_id);

      let exercise = AppObjects.workoutObject[exercise_id];
      ExerciseList.push(exercise);
    }
  }

  let cookie_mode = -1;
</script>

<div class="scrollSpecial">
  {#if saved_cookies.length == 0}
    <h6 class="display-7">You have no saved workouts.</h6>
  {/if}

  <div class="row">
    <div class="col">
      <ul class="list-group list-group-flush">
        {#each saved_cookies as cookie, i}
          <li class="list-group-item bg-transparent liSpecial">
            <button
              class="btn btn-outline-secondary col text-secondary"
              on:click={() => {
                LoadExerciseList(i);
                cookie_mode = cookie_mode == i ? -1 : i;
              }}>Save {i}</button
            >
          </li>
        {/each}
      </ul>
    </div>
  </div>

  {#if cookie_mode != -1}
    <div class="row" out:fade={{ duration: 400 }} in:fade={{ duration: 200 }}>
      <div class="col">
        <p
          class="btn-outline-secondary disabled"
          data-bs-toggle="tooltip"
          data-bs-placement="top"
          title="For each exercise you wish to add to your workout, you can filter out muscle group, difficulty, required equipment and exercise type."
        >
          Your results:
        </p>
        <ul class="list-group list-group-flush">
          {#each ExerciseList as exercise, i}
            <li class="list-group-item bg-transparent liSpecial">
              <ExerciseItem
                ExerciseEntry={exercise}
                ExerciseIndex={ExerciseIndexList[i]}
                id={i}
                {AppObjects}
                template={TemplateList[i]}
              />
            </li>
          {/each}
        </ul>
      </div>
    </div>
  {/if}
</div>

<style>
  .liSpecial {
    border: 0 !important;
  }
  .scrollSpecial {
    overflow-y: auto;
    overflow-x: hidden;
    max-height: 65vh;
    margin-bottom: 500px !important;
  }
</style>
