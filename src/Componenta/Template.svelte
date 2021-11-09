<script>
    export let value = 0;
</script>


Template with value {value}

<button on:click={() => {value--;}}> - </button>
<button on:click={() => {value++;}}> + </button>