<?php

namespace App\Policies;

use App\Models\Tbl_Mahasiswa;
use App\Models\User;
use Illuminate\Auth\Access\HandlesAuthorization;

class TblMahasiswaPolicy
{
    use HandlesAuthorization;

    /**
     * Determine whether the user can view any models.
     *
     * @param  \App\Models\User  $user
     * @return \Illuminate\Auth\Access\Response|bool
     */
    public function viewAny(User $user)
    {
        //
    }

    /**
     * Determine whether the user can view the model.
     *
     * @param  \App\Models\User  $user
     * @param  \App\Models\Tbl_Mahasiswa  $tblMahasiswa
     * @return \Illuminate\Auth\Access\Response|bool
     */
    public function view(User $user, Tbl_Mahasiswa $tblMahasiswa)
    {
        //
    }

    /**
     * Determine whether the user can create models.
     *
     * @param  \App\Models\User  $user
     * @return \Illuminate\Auth\Access\Response|bool
     */
    public function create(User $user)
    {
        //
    }

    /**
     * Determine whether the user can update the model.
     *
     * @param  \App\Models\User  $user
     * @param  \App\Models\Tbl_Mahasiswa  $tblMahasiswa
     * @return \Illuminate\Auth\Access\Response|bool
     */
    public function update(User $user, Tbl_Mahasiswa $tblMahasiswa)
    {
        //
    }

    /**
     * Determine whether the user can delete the model.
     *
     * @param  \App\Models\User  $user
     * @param  \App\Models\Tbl_Mahasiswa  $tblMahasiswa
     * @return \Illuminate\Auth\Access\Response|bool
     */
    public function delete(User $user, Tbl_Mahasiswa $tblMahasiswa)
    {
        //
    }

    /**
     * Determine whether the user can restore the model.
     *
     * @param  \App\Models\User  $user
     * @param  \App\Models\Tbl_Mahasiswa  $tblMahasiswa
     * @return \Illuminate\Auth\Access\Response|bool
     */
    public function restore(User $user, Tbl_Mahasiswa $tblMahasiswa)
    {
        //
    }

    /**
     * Determine whether the user can permanently delete the model.
     *
     * @param  \App\Models\User  $user
     * @param  \App\Models\Tbl_Mahasiswa  $tblMahasiswa
     * @return \Illuminate\Auth\Access\Response|bool
     */
    public function forceDelete(User $user, Tbl_Mahasiswa $tblMahasiswa)
    {
        //
    }
}
