
$(document).ready(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        }
    });
    campusModal();
    getCampuses();
    saveCampus();
    editCampus();
    deleteCampus();
    searchCounty();
    countyChange();
    //classChange();
})
function campusModal() {
    $('#open-modal').click(function () {
        clearData()
        $('#campusModal').modal({backdrop: 'static', keyboard: false})
    })

}
function clearData(){
      $('#county-frm').empty();
      $('#county-code').val('');
      $('#campus-form')[0].reset();
      $('#campus_code').val('');
}
function deleteCampus() {
    $('#campusTable').on('click','.btn-deleteCampus',function (s) {
        var data = $(this).closest('tr').find('#delete-campus').val();
        bootbox.confirm("Are you sure want to delete this Campus?", function (result) {
            if (result) {
               $.ajax({
            type: 'GET',
            url: 'deleteCampus/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
          bootbox.hideAll()
          getCampuses()
          bootbox.alert(s.success)


        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
            }
        })
    })
}

function getCampuses() {
     $.ajax({
        type: 'GET',
        url: 'getCampuses',
        processData: false,
        contentType: false,
    }).done(function (s) {
       $('#campusTable').DataTable().destroy();
       $("#campusTable tbody").empty();
        if(s.length!==0) {
            $.each(s, function (i, item) {
                $("#campusTable tbody").append(
                    "<tr scope='col'>"
                    + "<td>" + item.campus_code + "</td>"
                    + "<td>" + item.campus_name + "</td>"
                    + "<td>" + item.campusCounty + "</td>"
                    + "<td>" + item.campus_location + "</td>"
                    + "<td>" + item.campus_incharge + "</td>"
                    + "<td>" + item.campus_incharge_contacts + "</td>"
                    + "<td>" + '<form id="editCampus" method="post" enctype="multipart/form-data"><input type="hidden" id="edit-campus" name="id" value=' + item.campus_code + '></form><button class="btn btn-outline-primary btn-sm btn-editCampus" ><i class="fa fa-edit"></button>'
                    + "</td>"
                    + "<td>" + '<form id="deleteCampus" method="post" enctype="multipart/form-data"><input type="hidden" id="delete-campus" name="id" value=' + item.campus_code + '></form><button class="btn btn-outline-danger btn-sm btn-deleteCampus" ><i class="fa fa-trash-o"></button>'
                    + "</tr>")
            })
        }
        $('#campusTable').DataTable();
    }).fail(function (xhr, error) {
       bootbox.alert(xhr.responseText);
    });

}

function saveCampus(){
    $('#saveCampus').click(function () {
        var data=$('#campus-form').serialize();
        var url = '';
        if($('#campus_code').val()===''){
          url = 'createCampus'
        }else{
            url = 'updateCampus/'+$('#campus_code').val()
        }
		$.ajax({
			type: 'POST',
			url: url,
            data: data
		}).done(function (s) {
		    getCampuses()
            clearData()
            $('#campusModal').modal('hide')
			bootbox.alert(s.success)

		}).fail(function (xhr, error) {
						bootbox.alert(xhr.responseText)
            // bootbox.alert("Error Occured while saving")
		})


	})
}
function editCampus(){
    $('#campusTable').on('click','.btn-editCampus',function (s) {
        var data=$(this).closest('tr').find('#edit-campus').val();
        $.ajax({
            type: 'GET',
            url: 'editCampus/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
            $('#campus_code').val(s.campus_code);
            $('#campus_name').val(s.campus_name);
            $('#campus_location').val(s.campus_location);
            $('#campus_incharge').val(s.campus_incharge);
            $('#campus_incharge_contacts').val(s.campus_incharge_contacts);


            if (s.campusCountyCode) {
                $('#county-code').val(s.campusCountyCode)

                var $newOption = $("<option selected='selected' value='" + s.campusCountyCode + "'>'+s.campusCountyName+'</option>").val(s.campusCountyCode.toString()).text(s.campusCountyName)

                $('#county-frm').append($newOption).trigger('change');
            } else {
                $('#county-code').val('')

                $('#county-frm').empty();

            }

        $('#campusModal').modal({backdrop: 'static', keyboard: false})
        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
    });

}
function searchCounty() {
     $('#county-frm').select2({
           placeholder: 'Counties',
           allowClear: true,
           width: '100%' ,
           ajax: {
             delay: 250,
             url: 'searchCounty',
             data: function (params) {
                 console.log("AA", params);
                 return {
                     query: params.term,
                     gotoPage: params.page
                 }
             },

             processResults: function (data,params) {
                 params.page = params.page || 1;
                 console.log('data: ', data);
                 return {
                   results: data.results
                 };
             }

         }
     })
}

function countyChange(){
    $('#county-frm').on('select2:select', function (e) {
    var data = e.params.data;
    $('#county-code').val(data.id)
    $('#county-name').val(data.text)

});
    $("#county-frm").on("select2:unselecting", function(e) {
    $('#county-code').val('')
    $('#county-name').val('')
 });
}
