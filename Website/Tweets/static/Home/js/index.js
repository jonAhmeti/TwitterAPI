$(function() {

    const selectCountry = $("select[name='country']");
    const selectCity = $("select[name='selectCity']");
    const radius = $("input[name='radius']");

    $("input[name='byPlace']").on('change', function () {
        if ($(this).prop('checked')){
            $(selectCountry).prop('disabled', false);
            $(selectCity).prop('disabled', false);
            $(radius).prop('disabled', false)

        }else{
            $(selectCountry).prop('disabled', true);
            $(selectCity).prop('disabled', true);
            $(radius).prop('disabled', true)
        }
        console.log( $(this).prop('checked'));
    });

    $(selectCountry).on('change', function () {
        if( $(this).val() || $(this).val() !== ''){
            console.log('Selected country: ', $(this).val());
            $.ajax({
                type: 'GET',
                url: 'cities',
                data: {country: $(this).val()},
                success: function (result) {
                    let options = '';
                    for (let element of result){
                        options += `<option value="${element[0]}">${element[1]}</option>`
                    }
                    $(selectCity).html(options);
                },
                error: function (error) {
                    console.log('Something went wrong.', error);
                }
            });
        }else{
            //undefined, null or empty string
        }
    });

});