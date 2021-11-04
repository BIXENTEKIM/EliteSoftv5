
$(document).ready(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        }
    });
    sgModal();
    getSubjectGroups();
    saveSubjectGroup();
    editSubjectGroup();
    deleteSubjectGroup();
    //searchSubject();
    searchSubject();
    subjectChange();
    //classChange();
    //deleteSubject();
})
function sgModal() {
    $('#open-modal').click(function () {
        clearData()
        $('#sgModal').modal({backdrop: 'static', keyboard: false})
    })

}
function clearData(){
      $('#subject-frm').empty();
      $('#subject-code').val('');
      $('#sg-form')[0].reset();
      $('#sg_code').val('');
}
function deleteSubjectGroup() {
    $('#sgTable').on('click','.btn-deleteSubjectGroup',function (s) {
        var data = $(this).closest('tr').find('#delete-subjectgroup').val();
        bootbox.confirm("Are you sure want to delete this Subject Group?", function (result) {
            if (result) {
               $.ajax({
            type: 'GET',
            url: 'deleteSubjectGroup/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
          bootbox.hideAll()
          getSubjectGroups()
          bootbox.alert(s.success)


        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
            }
        })
    })
}

function getSubjectGroups() {
     $.ajax({
        type: 'GET',
        url: 'getSubjectGroups',
        processData: false,
        contentType: false,
    }).done(function (s) {
       $('#sgTable').DataTable().destroy();
       $("#sgTable tbody").empty();
        if(s.length!==0) {
            $.each(s, function (i, item) {
                $("#sgTable tbody").append(
                    "<tr scope='col'>"
                    + "<td>" + item.subjectgroupSubject + "</td>"
                    + "<td>" + item.sg_group + "</td>"
                    + "<td>" + item.sg_compulsory_f12 + "</td>"
                    + "<td>" + item.sg_compulsory_school + "</td>"
                    + "<td>" + '<form id="editSubjectGroup" method="post" enctype="multipart/form-data"><input type="hidden" id="edit-subjectgroup" name="id" value=' + item.sg_code + '></form><button class="btn btn-outline-primary btn-sm btn-editSubjectGroup" ><i class="fa fa-edit"></button>'
                    + "</td>"
                    + "<td>" + '<form id="deleteSubjectGroup" method="post" enctype="multipart/form-data"><input type="hidden" id="delete-subjectgroup" name="id" value=' + item.sg_code + '></form><button class="btn btn-outline-danger btn-sm btn-deleteSubjectGroup" ><i class="fa fa-trash-o"></button>'
                    + "</tr>")
            })
        }
        $('#sgTable').DataTable();
    }).fail(function (xhr, error) {
       bootbox.alert(xhr.responseText);
    });

}

function saveSubjectGroup(){
    $('#saveSubjectGroup').click(function () {
        var data=$('#sg-form').serialize();
        var url = '';
        if($('#sg_code').val()===''){
          url = 'createSubjectGroup'
        }else{
            url = 'updateSubjectGroup/'+$('#sg_code').val()
        }
		$.ajax({
			type: 'POST',
			url: url,
            data: data
		}).done(function (s) {
		    getSubjectGroups()
            clearData()
            $('#sgModal').modal('hide')
			bootbox.alert(s.success)

		}).fail(function (xhr, error) {
						bootbox.alert(xhr.responseText)
            // bootbox.alert("Error Occured while saving")
		})


	})
}
function editSubjectGroup(){
    $('#sgTable').on('click','.btn-editSubjectGroup',function (s) {
        var data=$(this).closest('tr').find('#edit-subjectgroup').val();
        $.ajax({
            type: 'GET',
            url: 'editSubjectGroup/'+data,
            processData: false,
            contentType: false,
        }).done(function (s) {
            $('#sg_code').val(s.sg_code);
            $('#sg_group').val(s.sg_group);
            //alert(s.subjectIncludeForPos);
            if (s.sg_compulsory_school === true) {
                $('#sg_compulsory_school').prop('checked', true);
            }
            else {
                $('#sg_compulsory_school').prop('checked', false);

            }

            if (s.sg_compulsory_f12 === true) {
                $('#sg_compulsory_f12').prop('checked', true);
            }
            else {
                $('#sg_compulsory_f12').prop('checked', false);

            }


            if (s.subjectGroupSubjectCode) {
                $('#subject-code').val(s.subjectGroupSubjectCode)

                var $newOption = $("<option selected='selected' value='" + s.subjectGroupSubjectCode + "'>'+s.subjectGroupSubjectName+'</option>").val(s.subjectGroupSubjectCode.toString()).text(s.subjectGroupSubjectName)

                $('#subject-frm').append($newOption).trigger('change');
            } else {
                $('#subject-code').val('')

                $('#subject-frm').empty();

            }

        $('#sgModal').modal({backdrop: 'static', keyboard: false})
        }).fail(function (xhr, error) {
        bootbox.alert(xhr.responseText)
        });
    });

}
function searchSubject() {
     $('#subject-frm').select2({
           placeholder: 'Subjects',
           allowClear: true,
           width: '100%' ,
           ajax: {
             delay: 250,
             url: 'searchSubject',
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
//function searchClasses() {
//     $('#class-frm').select2({
//           placeholder: 'Classes',
//           allowClear: true,
//           width: '100%' ,
//           ajax: {
//             delay: 250,
//             url: 'searchclasses',
//             data: function (params) {
//                 console.log("AA", params);
//                 return {
//                     query: params.term,
//                     gotoPage: params.page
//                 }
//             },
//
//             processResults: function (data,params) {
//                 params.page = params.page || 1;
//                 console.log('data: ', data);
//                 return {
//                   results: data.results
//                 };
//             }
//
//         }
//     })
//}
function subjectChange(){
    $('#subject-frm').on('select2:select', function (e) {
    var data = e.params.data;
    $('#subject-code').val(data.id)
    $('#subject-name').val(data.text)

});
    $("#subject-frm").on("select2:unselecting", function(e) {
    $('#subject-code').val('')
    $('#subject-name').val('')
 });
}
//function classChange(){
//    $('#class-frm').on('select2:select', function (e) {
//    var data = e.params.data;
//    $('#next-id').val(data.id)
//    $('#next-name').val(data.text)
//
//});
//    $("#class-frm").on("select2:unselecting", function(e) {
//    $('#next-id').val('')
//    $('#next-name').val('')
// });
//}
